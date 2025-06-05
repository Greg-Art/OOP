
##intro:

"""

This section focuses on how we can create a class and the various components of a class such as:

- instance/object
- arugments
- methods and many others 

"""

## creating a dog class 

class Dog:
    def bark(self):
        print("woof woof")

##creating an object 

dog1= Dog()

##access the bark method 
dog1.bark()


##adding some attribute to the dog class 

class Dog:
    ##creating an init method to declare the arguments our class can take 
    def __init__(self, name, breed):
        self.name= name
        self.breed= breed
    ##
    def bark(self):
        print("woof woof")
    

dog1= Dog("JJ", "Dobberman")

dog2= Dog("Rody", "German Sheperd")


dog1.breed

##we are defining  a class for dog owners 

class Owner:

    def __init__(self, name, address, contact_number):
        self.name= name 
        self.address= address
        self.contact_number= contact_number


##next, we will rewrite our Dog class to add a parameter for owner

class Dog:
    ##creating an init method to declare the arguments our class can take 
    def __init__(self, name, breed, owner):
        self.name= name
        self.breed= breed
        self.owner= owner
    ##
    def bark(self):
        print("woof woof")


##now I will creaete an owner instance 

owner1= Owner("Gregory", "989 Alex Turkson Street", "999-515-207")

##we will pass the above instance as an argument to our new Dog instance 

dog3= Dog("Rhino", "Rotweiller", owner1)

##we will pring the owner's name
dog3.owner.name

## let create another own instance and dog instance

owner2= Owner("Aiko", "123 77street", "0244578738") ##owner instance

dog4= Dog("Piper", "Poodle", owner2) ##dog instance

dog4.owner.name
dog4.owner.address

## we are just trying again

class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age 

    def greet(self):
        print(f"my name is {self.name} and I am {self.age} years old") ## here I am using a string fort


person= Person("kwaku", 23)

person.greet()

## Summary notes:

"""

-  name and age: These are referred to as parameters

- self is used to refer to the current object of the class 

- self.name= name and self.age= age are attributes

- def__init__ and def greet are methods (functions in a class)

- def__init__: This is a special method that allows us to accept inputs and asign them to specific objects during instantiating

"""