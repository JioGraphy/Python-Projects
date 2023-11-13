
# Parent Class
class Robot:

    def __init__(self, name):
        self.name = name
        self.position = [0, 0]
        print('My name is', self.name)
   
    def walk(self, x):
        self.position[0] = self.position[0] + x
        print('New Position:', self.position)

    def eat(self):
        print('Hungry')


# Child Class
class RobotDog(Robot):

    '''
    Inherited parent class init method by default, if there's no init implementation
    of the child class
    '''

    def make_noise(self):
        print('Woof Woof!')


    # method overriding
    def eat(self):
        super().eat() # accessing parent class method using super method
        print('I like bacon')
     


# # Main Program
# def main():
#     # Calling the constructor and passing the value in var
#     my_robot_dog = Robot_Dog('Marley')
#     my_robot_dog.walk(10)
#     my_robot_dog.make_noise()


# main()

my_robot_dog = RobotDog('Bud')
my_robot_dog.walk(10)
my_robot_dog.make_noise()
my_robot_dog.eat()