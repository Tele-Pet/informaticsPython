# Finds files of a certain type, then copies them to new folder in the parent directory

import glob, os, shutil

source_dir = "/Users/josiah_MBP/Desktop/sourceFolder/"
dest_dir = "/Users/josiah_MBP/Desktop/destinationFolder/"

# files = glob.iglob(os.path.join(source_dir, "*.txt"))
# for file in files:
#     if os.path.isfile(file):
#         shutil.copy2(file, dest_dir)

toCopyList = []
for root, dirs, files in os.walk(source_dir):
    for name in files:
        if name.endswith(".png"):
       		print name
       		# Can't currently figure out how to copy noted files

