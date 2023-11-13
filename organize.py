import os
import shutil
import datetime


# Path of the desktop folder
# ~ tilde replace the users home directory
# replaces /Users/george.estellore.iii/ to ~ 
desktop_path = os.path.expanduser("~/Desktop") 
# print('Desktop Path:', desktop_path)


# Dictionary containing the folder names and their corresponding file extension
folders = {
    "Images": [".jpeg", ".jpg", ".png", ".gif"],
    "Documents": [".doc", ".docx", ".pdf", ".txt"],
    "Archives": [".zip", ".rar"]
}


# Create the subfolders if they don't exist
for folder_name in folders: # Loops over dictionaries defaults to keys

    '''
    Make absolute path to the new folder using os.path.join
    Ex: /Users/george.estellore.iii/
    '''
    folder_path = os.path.join(desktop_path, folder_name) 
    # print('Folder Path: ',  folder_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


# Move files to the corresponding folders
for file_name in os.listdir(desktop_path): # list all the entries(files or folders) on the Desktop/
    original_file_path = os.path.join(desktop_path, file_name)
    # print(file_path)

    # Check if original path file is a file a not folder, we dont want to move directories only files
    if os.path.isfile(original_file_path): 
        for folder_name, extensions in folders.items(): # Loops over in 'folders' every key:value pairs
            for extension in extensions: # Loop over all of the extensions in each dictionary
                if file_name.endswith(extension): # if current file name ends with current extension
                    destination_folder = os.path.join(desktop_path, folder_name) # points to extension's corresponding folder_name
                    # print('Successfully Executed! ')
                    # print('FROM:', original_file_path, '--->', 'MOVE TO:', destination_folder)
                    shutil.move(original_file_path, destination_folder) # move the current file to the new destination folder



current_datetime = datetime.datetime.now()

logs_txt = 'Logs.'+ current_datetime +'.txt'

with open(logs_txt, 'a') as file:

    orig_path = '~/Desktop/Others/Python/sandbox/Projects'
    os.path.join(desktop_path, file_name)
    
    destination_path  = '~/Desktop/Others/Python/sandbox/Projects/files'
    shutil.move(orig_path, desktop_path)

    file.write()