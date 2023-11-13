# Important to know: Orders matter in the program
# function needs to be defined first, before calling it.
# Variables: Local Scope and Global Scope
# Function used to organize our code into logical units

global_var = input('Enter your name: \n')


# function definition
def greeting_local(local_name):
    print('\nLocal Scope Variable')
    print('Hello ' + local_name)


# function definition
def greeting_global():
    print('\nGlobal Scope Variable')
    print('Hello ' + global_var)


def addition(a, b):
    c = a + b
    print(c)
    return c


# Main Program
def main():
    input_name = input('Enter your name: \n')
    num1 = int(input('Enter 1st Number: '))
    num2 = int(input('Enter 2nd Number: '))

    greeting_local(input_name)
    greeting_global()
    addition(num1, num2)


# Invoking main function
main()
