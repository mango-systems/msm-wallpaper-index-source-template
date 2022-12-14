# # import os
# # import json

# # folder = "wallpaper"

# # # Get all filenames in the folder
# # filenames = os.listdir(folder)

# # # Create a dictionary with the filenames and their modified versions
# # data = {}
# # for filename in filenames:
# #   data[filename] = {
# #     "thumbnail": "abc.xyz/" + filename,
# #     "main_file": "yui.oiu/" + filename
# #   }

# # # Write the data to a JSON file
# # with open("index.json", "w") as f:
# #   json.dump(data, f)

# import os
# import json

# folder = "wallpaper"

# # Get all filenames in the folder
# filenames = os.listdir(folder)

# # Rename all the filenames to remove spaces and replace them with underscores
# for filename in filenames:
#   new_filename = filename.replace(" ", "_")
#   os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))

# # Create a dictionary with the filenames and their modified versions
# data = {}
# for filename in filenames:
#   data[filename] = {
#     "abc.xyz": "abc.xyz" + filename,
#     "yui.oiu": "yui.oiu" + filename
#   }

# # Write the data to a JSON file (overwriting the file if it exists)
# with open("index.json", "w") as f:
#   json.dump(data, f)

# ## remove the extension name part from the fie name


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
    thumbnail_filename = filename.replace(".jpg", "-thumbnail.jpg")
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
