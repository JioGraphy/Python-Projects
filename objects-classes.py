
class RobotDog:

    # init method initialize the class properties
    '''
    self keyword refers to the INSTANCE OF THE CLASS that
    were creating or the current object
    '''
    def __init__(self, name_val, breed_val):
        self.name = name_val
        self.breed = breed_val

    # Method is a function that belongs to a class
    def bark(self):
        print('Woof Woof')


# Main Program
my_dog = RobotDog('Marley', 'Aspin')


# dot lets you access the properties
print('Dog Breed: {}'.format(my_dog.breed))
print('Dog Name: {}'.format(my_dog.name))
my_dog.bark()