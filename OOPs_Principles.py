"""In this section, we will take a look at the core principles of OOPS.These include:

- Encapsulation

- Polymorphism

- Inheritance

- Abstraction

"""


##Encapsulation

class BadBankAccount:
    def __init__(self, balance):
        self.balance= balance


account= BadBankAccount(20000)

account.balance= (-2000)

print(account.balance)

## as we have seen previously, this type of programming leads to methods and attributes been changeable 


##let's recreate another good example 
class BankAccount:
    def __init__(self):
        self._balance= 0.00 ## we are making this protected, we are encapsulating it 

    @property ## we are protecting the balance to ensure one cannot directly change it 
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount >0:
            self._balance += amount
            return f"Your new balance is ${self._balance}" 
        raise ValueError("Deposit amount my be positive")
    
    def withdrawal(self, amount):
        if self._balance > amount:
            self._balance-= amount
            return f"Your new balance is ${self._balance}" 
        raise ValueError("Insufficient funds: Withdrawal amount exceeds balance")


account= BankAccount()

account.deposit(1000)

print(account.balance)

account.withdrawal(400)

print(account.balance)

"""
Here we can see that we used encapsulation to:

- Prevent users from changing bank account details when accessing their account we used a getter method for this

- We ensured the user could only use the deposit and withdrawal methods for depositing and withdrawing cash. With that, we even specified the rules 

- For cleaner code, we used the raise ValueError to handle how errors are made

"""


##Abstraction

## We use abstraction to hide unecessary details 

class EmailService:

    def _connect(self):
        print("Connecting to email server")

    def _authenticate(self):
        print("authenticating")
    
    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending email")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server.....")

first_email= EmailService()

first_email.send_email()

"""

- Here we have abstracted the email sending process by ensuring that the user can just hit send_email and the email is sent. They do not need to individually call the:
 - Connect
 - Authentication
 - Disconnect 
Methods as we have absracted and handled them in the send email method

"""


## Inheritance 

#Inheritance is a concept in OOPs that involves creating a new class based on an existing one

class Vehicle:
    
    def __init__(self, brand, model, year):
        self.brand= brand
        self.model= model 
        self.year= year
    
    def start(self):
        print(f"Your vehicle is starting")

    def stop(self):
        print(f"Your vehicle is stopping")

class Car(Vehicle): ##this is a subclass inheriting from Vehicle
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year) ##this is to indicate which attributes we are inheriting from the parent class
        self.number_of_doors= number_of_doors
        self.number_of_wheels= number_of_wheels


class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year) ##this is to indicate which attributes we are inheriting from the parent class
        self.number_of_wheels= number_of_wheels


car1= Car("Toyota", "Corolla 2021", 1998, 2, 4)

bike1= Bike("Honda", "Scoopy", 2018, 3)

print(car1.__dict__)

print(bike1.__dict__)

bike1.start() ##using the start method from


##Polymorphism 

## this is the ability of an object to take many forms

class Car:
    
    def __init__(self, brand, model, year, no_of_doors):
        self.brand= brand
        self.model= model 
        self.year= year
    
    def start(self):
        print(f"Your vehicle is starting")

    def stop(self):
        print(f"Your vehicle is stopping")

class Motorcycle:
    
    def __init__(self, brand, model, year):
        self.brand= brand
        self.model= model 
        self.year= year
    
    def start_bike(self):
        print(f"Your vehicle is starting")

    def stop_bike(self):
        print(f"Your vehicle is stopping")

vehicles= [

    Car("Ford", "Focus", 2018, 5),

    Motorcycle("Honda", "Scoppy", 2020)


]

for vehicle in vehicles:
    if isinstance(vehicle, Car):
        print(f"vehic")