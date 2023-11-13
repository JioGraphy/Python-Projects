
# file = open('acronyms.txt')

# with open('acronyms.txt') as file:
#     # Do file operations here

# file = open('acronyms.txt')

# file = open('acronyms.txt')
# try:
#      # Do file operations here
#      pass
# finally:
#      file.close()


# with open('files/acronyms.txt') as file:
#     result = file.read()
#     print(result)


# with open('files/acronyms.txt') as file:
#     result = file.readlines()
#     print(result)


# with open('files/acronyms.txt') as file:
#     result = file.readlines()
#     for line in result:
#         print(line)

def find_acronym():

    look_up = input('What acronym would you like to look up? \n')
    found = False

    try:
        with open('files/acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as err:
        print(err, 'File not found it can be RENAME, MOVE or DELETED')
        print('Please check the files directory or file name ')
        return

    if not found:
        print('The acronym does not exist')


def add_acronym():
    acronym = input('What acronym you want to add? \n')
    definition = input('What definition you want to add? \n')


    # w - write mode, existing file with the same name will be erased, overwrite
    # with open('files/acronyms.txt', 'w') as file:
    #     file.write(acronym + ' - ' + definition + '\n')


    with open('files/acronyms.txt', 'a', encoding='utf-8') as file:
        file.write(acronym + ' - ' + definition + '\n')


def main():

    choice = input('Do you want to find(F) or Add(A) an acronym? ')

    while True:

        if choice == 'F':
            find_acronym()
            break
        elif choice == 'A':
            add_acronym()
            break
        else: 
            raise ValueError('Please input valid choice')
            
 

try:
    main()
except KeyboardInterrupt as e:
    print('\n Program interrupted. Exiting Program...')
