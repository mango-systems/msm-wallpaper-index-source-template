# MSM Wallpaper index
This is where I host all my wallpapers and store them in a index.json so it can be fetched by a client app and show all the wallpapers into a one place

## Instructions to add wallpaper

```bash
git clone https://github.com/msm-linux/msm-wallpaper-index-source.git

# then add the wallpapers to the "wallpaper" folder
#       ## < ADD YOUR IMAGES in "wallpaper" folder > ##
# then run

pip install -r requirements.txt
chmod +x build.py
python3 build.py

# then push the updated wallpapers to repo
git add -all
git commit -m "updated/added wallpaper"
git push
```

## What does this script does?
    - renames the file name to replace "space" with "underscore"
    - generates thumnails
    - generates a index.json file with thumbnail link and then the main file link, that is to be fetched by client app 

