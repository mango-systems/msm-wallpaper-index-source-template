# import os
# import json

# # Set the directory you want to rename files in
# dir_name = "./wallpaper"

# # Create a dictionary to store the old and new filenames
# filenames = {}

# # Loop through the files in the directory
# for filename in os.listdir(dir_name):
#   # Get the full path of the file
#   file_path = os.path.join(dir_name, filename)
#   # Create the new filename by replacing spaces with underscores
#   new_filename = filename.replace(" ", "_")
#   # Get the full path of the new file
#   new_file_path = os.path.join(dir_name, new_filename)
#   # Rename the file
#   os.rename(file_path, new_file_path)
#   # Add the old and new filenames to the dictionary
#   filenames[filename] = new_filename

# # Write the filenames to a JSON file
# with open("wallpaper-index.json", "w") as f:
#   json.dump(filenames, f)


import os
import json
from PIL import Image

# Set the directory you want to rename files in
dir_name = "wallpaper"

# Create a directory to store the thumbnails
thumbnail_dir = "wallpaper-thumbnails"
if not os.path.exists(thumbnail_dir):
  os.makedirs(thumbnail_dir)

# Create a dictionary to store the old and new filenames
filenames = {}

# Loop through the files in the directory
for filename in os.listdir(dir_name):
  # Get the full path of the file
  file_path = os.path.join(dir_name, filename)
  # Open the image file
  im = Image.open(file_path)
  # Create a thumbnail image with medium size
  im.thumbnail((300, 300))
  # Save the thumbnail to the specified directory
  im.save(os.path.join(thumbnail_dir, filename))
  # Create the new filename by replacing spaces with underscores
  new_filename = filename.replace(" ", "_")
  # Get the full path of the new file
  new_file_path = os.path.join(dir_name, new_filename)
  # Rename the file
  os.rename(file_path, new_file_path)
  # Add the old and new filenames to the dictionary
  filenames[filename] = new_filename

# Write the filenames to a JSON file
with open("wallpaper-index.json", "w") as f:
  json.dump(filenames, f)
