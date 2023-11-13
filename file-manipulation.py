# access to the os, file, directories
import os


# Absolute full path
# create a folder
# make_folder = os.mkdir('/Users/george.estellore.iii/Desktop/NewFolder')

try:

    folder_original = ('/Users/george.estellore.iii/Desktop/')
    folder_destination = ('/Users/george.estellore.iii/Desktop/CleanedUp')

    location_original = os.path.join(folder_original, 'new.txt')
    location_destination = os.path.join(folder_destination, 'new.txt')

    # rename func allows us to rename and move file to a new path 
    os.rename(location_original, location_destination)

    # entries = os.scandir(folder_destination)

    entries = os.scandir(folder_original)

    # Create an absolute path from a path string and a file name
    new_name = os.path.join(folder_destination, 'new.txt')

    # Iterate entries(files/folders) on the folder
    for entry in entries:
        if os.path.isfile(entry):
            print('File:', entry.name)
        elif os.path.isdir(entry):
            print('Directory:', entry)

except FileNotFoundError as err:
    print(err, 'Directory not found! \n Please check the path')
