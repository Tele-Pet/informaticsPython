sourceFile = "/Users/josiah_MBP/Desktop/testFolder/this is a text file.txt"
destinationFolder = "/Users/josiah_MBP/Desktop/testFolder/testDestination/"

import shutil

shutil.copy2(sourceFile, destinationFolder)
print 'done'