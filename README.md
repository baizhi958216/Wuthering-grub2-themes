![banner](banner.png?raw=true)

## Installation:

Usage:  `sudo ./install.sh [OPTIONS...]`

```
  -t, --theme     Background theme variant(s) [changli|jinxi|jiyan|yinlin|anke|weilinai|kakaluo|jianxin|qianxiao|qianxian|cartethyia|younuo|aemeath|lynae|mornye] (default is changli; qianxian is an alias for qianxiao)
  -s, --screen    Screen display variant(s)   [1080p|2k|4k|auto] (default is 1080p)
  -r, --remove    Remove/Uninstall theme      [changli|jinxi|jiyan|yinlin|anke|weilinai|kakaluo|jianxin|qianxiao|qianxian|cartethyia|younuo|aemeath|lynae|mornye] (must add theme name option, default is changli)
  -b, --boot      install theme into '/boot/grub' or '/boot/grub2'
  -h, --help      Show this help
```

_If no options are used, a user interface `dialog` will show up instead_

### Examples:

`qianxian` is accepted as a compatibility alias for the bundled `qianxiao`
theme. Both commands install the same theme directory and assets:

```sh
sudo ./install.sh -t qianxian -s 4k
sudo ./install.sh -t qianxiao -s 4k
```

 - Install yinlin theme on 2k display device:

```sh
sudo ./install.sh -t yinlin -s 2k
```

 - Install jinxi theme into /boot/grub/themes:

```sh
sudo ./install.sh -b -t jinxi
```

 - Uninstall yinlin theme:

```sh
sudo ./install.sh -r -t yinlin
```

## Issues / tweaks:

### Background compatibility fix:

GRUB supports baseline JPEG images but may fail to decode progressive JPEGs. The
`aemeath`, `lynae`, `mornye`, and `younuo` backgrounds have been re-encoded as
baseline JPEGs so these themes load without requiring ImageMagick during
installation. Run `python3 tests/check-backgrounds.py` to verify all bundled
backgrounds before creating a release.

### Correcting display resolution:

 - On the grub screen, press `c` to enter the command line
 - Enter `vbeinfo` or `videoinfo` to check available resolutions
 - Open `/etc/default/grub`, and edit `GRUB_GFXMODE=[width]x[height],auto` to match your resolution
 - Finally, run `grub-mkconfig -o /boot/grub/grub.cfg` to update your grub config

### Setting a custom background:

 - Make sure you have `imagemagick` installed, or at least something that provides `convert`
 - You can use `-s auto` to auto-detect display resolution and center-crop background to fit
 - If you use fixed modes (`1080p`, `2k`, `4k`), background should match that target resolution
   - 1920x1080 >> 1080p
   - 2560x1440 >> 2k
   - 3840x2160 >> 4k
 - Place your custom background inside the root of the project, and name it `background.jpg`
 - Run the installer with `-t [THEME] -s auto` (recommended), or choose a fixed mode with `-s [1080p|2k|4k]`

## Contributing:
 - If you made changes to icons, or added a new one:
   - Delete the existing icon, if there is one
   - Run `cd assets; ./render-all.sh`
 - Before committing a background, run `python3 tests/check-backgrounds.py`.
   GRUB requires baseline JPEG files and cannot load progressive JPEG backgrounds.
 - Create a pull request from your branch or fork
 - If any issues occur, report then to the [issue](issues) page

## Preview:

Generated from real boot simulation (`QEMU + UEFI + GRUB`), then compressed for GitHub display.

### 2560x1440

| changli | jinxi | jiyan | yinlin |
|---|---|---|---|
| ![changli 2560x1440](previews/preview-qemu-changli-2560x1440.jpg) | ![jinxi 2560x1440](previews/preview-qemu-jinxi-2560x1440.jpg) | ![jiyan 2560x1440](previews/preview-qemu-jiyan-2560x1440.jpg) | ![yinlin 2560x1440](previews/preview-qemu-yinlin-2560x1440.jpg) |

| anke | weilinai | kakaluo | jianxin |
|---|---|---|---|
| ![anke 2560x1440](previews/preview-qemu-anke-2560x1440.jpg) | ![weilinai 2560x1440](previews/preview-qemu-weilinai-2560x1440.jpg) | ![kakaluo 2560x1440](previews/preview-qemu-kakaluo-2560x1440.jpg) | ![jianxin 2560x1440](previews/preview-qemu-jianxin-2560x1440.jpg) |

### 2560x1600

| qianxiao | cartethyia | younuo |
|---|---|---|
| ![qianxiao 2560x1600](previews/preview-qemu-qianxiao-2560x1600.jpg) | ![cartethyia 2560x1600](previews/preview-qemu-cartethyia-2560x1600.jpg) | ![younuo 2560x1600](previews/preview-qemu-younuo-2560x1600.jpg) |

| aemeath | lynae | mornye |
|---|---|---|
| ![aemeath 2560x1600](previews/preview-qemu-aemeath-2560x1600.jpg) | ![lynae 2560x1600](previews/preview-qemu-lynae-2560x1600.jpg) | ![mornye 2560x1600](previews/preview-qemu-mornye-2560x1600.jpg) |

## Documents

[Grub2 theme reference](https://wiki.rosalab.ru/en/index.php/Grub2_theme_/_reference)

[Grub2 theme tutorial](https://wiki.rosalab.ru/en/index.php/Grub2_theme_tutorial)
