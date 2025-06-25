# A class is a blueprint for creating objects(instances) that have atrributes(variables) ad methods(Functions). It acts as a template for creating the instances(objects) of similar charachteristics

# Creating a simple class
class Person:
    # Constructor method to initialize attributes
    def __init__(self, name="Sutapa", age=19, city="Howrah"):
        self.name = name
        self.age = age
        self.city = city
        # self.something means we want to access something from our class, which is an instance variable.
    def talk(self):
        print("Hello, I am a Sutapa")
    # use of self parameter
    def greet(self, name):
        print(f"'Hello! I am {self.name}, and I am {self.age} years old. I live in {self.city}.")
        # self is a reference to the current instance of the class, allowing access to its attributes and methods.
        # it is used to differentiate between instance variables and local variables within class methods.
        # It is the first parameter of any method in a class, and it is automatically passed when the method is called on an instance of the class.
    
# Creating an instance of the class
sutapa = Person("Jordan",20,"New York")  # Creating an instance of the Person class with specific attributes
sutapa.talk()  # Calling the method of the class