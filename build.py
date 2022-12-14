import os
import json
from PIL import Image

folder = "wallpaper"
thumbnail_folder = "wallpaper-thumbnail"

# Create the thumbnail folder if it does not already exist
if not os.path.exists(thumbnail_folder):
  os.mkdir(thumbnail_folder)

# Get all filenames in the folder
filenames = os.listdir(folder)

# Create a dictionary with the filenames and their modified versions
data = {}
for filename in filenames:
  # Open the image and create a thumbnail
  with Image.open(os.path.join(folder, filename)) as img:
    img.thumbnail((256, 256))

    # Save the thumbnail to the thumbnail folder
    filename_extension = "." + filename.split(".")[-1]
    renamed_filename = "-thumbnail" + "." + filename.split(".")[-1]
    thumbnail_filename = filename.replace(filename_extension, renamed_filename)
    img.save(os.path.join(thumbnail_folder, thumbnail_filename))

    # Add the thumbnail filename to the data dictionary
    data[filename] = {
      "filename": os.path.splitext(filename)[0],
      "highres_link": "abc.xyz" + filename,
      "thumbnail_file_link": "yui.oiu/wallpaper-thumbnail/" + thumbnail_filename
    }

# Write the data to a JSON file (overwriting the file if it exists)
with open("index.json", "w") as f:
  json.dump(data, f)
