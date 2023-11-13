# access to the os, file, directories
import os


# Absolute full path
# create a folder
# make_folder = os.mkdir('/Users/george.estellore.iii/Desktop/NewFolder')

try:

    folder_original = ('/Users/george.estellore.iii/Desktop/')
    folder_destination = ('/Users/george.estellore.iii/Desktop/CleanedUp-v2')

    os.mkdir(folder_destination) 

    for entry in os.scandir(folder_original):

        location_original = os.path.join(folder_original, entry.name)
        location_destination = os.path.join(folder_destination, entry.name)

        if os.path.isfile(location_original):
            os.rename(location_original, location_destination)
        
    print('Program Successfully executed')

except FileExistsError as err:
    print(err, 'Directory not found! \n Please check the path')