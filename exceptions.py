acronyms = {
            'LOL': 'Laugh out loud',
            'IDK': 'I dont know',
            'TBH': 'To be honest'
            }

# try:
#     # Code that might cause an exception
#     definition = acronyms['BTW'] 
# except:
#     # Print an error message
#     print('They key does not exist')


# # Program continues as usual after try except block
# print('The program keeps going...')


try:
    # Code that might cause an exception
    acr = acronyms['BTW'] 
    print('Definition of {} is {}'.format(acronyms, acr))
except KeyError as err:
    # Print an error message
    print(f'They key {err} does not exist')
finally:
    # finally block will be executed whether there was an error or not
    # can be used to close objects or clean up resources
    print('The acronyms we have define are: ')
    for acronym in acronyms:
        print(acronym)

print('The program keeps going')
 

def remainder_division(a, b):

    # Raising an exception
    # if b == 0:
    #     raise ZeroDivisionError
    
    # or 

    # Creating a custom Exception by calling Exception constructor
    if b == 0:
        raise ZeroDivisionError('Divisor cannot be 0')
    
    result = a // b
    remainder = a % b
    print(a, '/', b, 'is', result, 
          'remainder', remainder
          )


remainder_division(10, 0)



        
    # except ZeroDivisionError as err:
    #     print(err)