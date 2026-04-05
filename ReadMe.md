
# Image helper

## Prepare your environment

You will need python3 installed on your computer. For more info to install pythnon see <a href="https://www.python.org" target="_blank">here</a>.

If you have python3 already installed, run the following vommand to install python's Pillow library.

```bash
pip3 install Pillow --break-system-packages
```

## Download this repo

Download [ImageHelper.zip](https://github.com/thanasisgalanis/Image-Helpers/archive/refs/heads/main.zip) and extract it in any folder you wish in your PC (i.e. Heplers, Scripts, etc)

## Resize images
```bash
cd [The path the folder you extract the repo ImageHelpers.zip]
```

```bash
## Resize images to the given width (in pixels)
python3 resize.py "/Users/tgalanis/Downloads/ΕΤΟΙΜΑ SITE" 1200
```

```bash
## Resize images to the given width (in pixels)
## and forcing output to jpeg
python3 resize.py "/Users/tgalanis/Downloads/ΕΤΟΙΜΑ SITE" 1200 jpeg
```

```bash
## Resize images to the given width (in pixels),
## forcing output to jpeg
## and tranform greek characters to greeklish
python3 resize.py "/Users/tgalanis/Downloads/ΕΤΟΙΜΑ SITE" 1200 jpeg greeklish
```

## Modifications
Feel free to modify or improve this script and create a pull request with your changes.