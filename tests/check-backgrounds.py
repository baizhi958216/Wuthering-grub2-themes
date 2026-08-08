#!/usr/bin/env python3
"""Validate that theme backgrounds use the JPEG subset supported by GRUB."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
BACKGROUNDS = ROOT / "backgrounds"
BASELINE_SOF_MARKERS = {0xC0, 0xC1}
UNSUPPORTED_SOF_MARKERS = set(range(0xC2, 0xD0)) - {0xC4, 0xC8, 0xCC}


def jpeg_sof_marker(path: Path) -> int | None:
    data = path.read_bytes()
    if not data.startswith(b"\xff\xd8"):
        return None

    offset = 2
    while offset < len(data):
        while offset < len(data) and data[offset] != 0xFF:
            offset += 1
        while offset < len(data) and data[offset] == 0xFF:
            offset += 1
        if offset >= len(data):
            break

        marker = data[offset]
        offset += 1
        if marker in BASELINE_SOF_MARKERS | UNSUPPORTED_SOF_MARKERS:
            return marker
        if marker == 0xDA:  # Start of scan: no SOF marker was found.
            break
        if marker in {0x01, *range(0xD0, 0xDA)}:
            continue
        if offset + 2 > len(data):
            break

        segment_length = int.from_bytes(data[offset : offset + 2], "big")
        if segment_length < 2:
            break
        offset += segment_length

    return None


def main() -> int:
    failures = []
    for path in sorted(BACKGROUNDS.glob("background-*.jpg")):
        marker = jpeg_sof_marker(path)
        if marker not in BASELINE_SOF_MARKERS:
            description = "not a valid JPEG" if marker is None else f"unsupported SOF marker 0x{marker:02x}"
            failures.append(f"{path.relative_to(ROOT)}: {description}")

    if failures:
        print("GRUB-incompatible backgrounds:", file=sys.stderr)
        print("\n".join(f"- {failure}" for failure in failures), file=sys.stderr)
        return 1

    print("All theme backgrounds are baseline JPEG files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
