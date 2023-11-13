acronym = input('What acronym you want to add? \n')
definition = input('What definition you want to add? \n')


# w - write mode, existing file with the same name will be erased, overwrite
# with open('files/acronyms.txt', 'w') as file:
#     file.write(acronym + ' - ' + definition + '\n')


with open('files/acronyms.txt', 'a') as file:
    file.write(acronym + ' - ' + definition + '\n')