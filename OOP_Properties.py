"""

From our previous coverage of accessing objects, we could see that we could still access some protected and privat attributes 

However, we can use properties to control and limit the access we have to each attribute 

In this section, we will take a look at using:

- Getter properties: This will allow users to access the email but they cannot modify it 

- Setter properties 

This is more pythonic 

"""

##getter properties 

class Bank:
    def __init__(self, username, email, password, balance):
        self.username= username
        self._email= email ##we are protecting the email here
        self.__password= password ##we are privitizing the password 
        self.balance= balance 

    @property ##here we are creating a getter property 
    def email(self):
        print("Email accessed")
        return self._email 
    

user1= Bank("JamesKwaku", "jjjk@user.com", "75HyTT98", 171717623)

print(user1.email) ##with this, we are accessing the property instead of the email directly 

user1.email= "Yawadabo@gmail.com"

print(user1.email) 

##setter properties 


class Bank:
    def __init__(self, username, email, password, balance):
        self.username= username
        self._email= email ##we are protecting the email here
        self.__password= password ##we are privitizing the password 
        self.balance= balance 

    @property ##here we are creating a getter property 
    def email(self):
        print("Email accessed")
        return self._email 

    @email.setter #this is hwo we create a setter property
    def email(self, new_email):
        valid_values= (".com", ".org", ".edu")
        if '@' not in new_email or not new_email.endswith(valid_values): ## we are saying if the email is missing an @ or doesn't end with any of the specified domains
            raise Exception("Your email is missing either @ or .com") ##we should raise an error message
        self._email= new_email


## Static Attributes 

# A static attribute (are known as class attribute) is an attribute that belongs to the class itself 

class User:
    user_count= 0  ##class attribute or static attribute 
    
    def __init__(self, username, email): 
        self.username= username ##these are instance attributes 
        self.email= email 
        User.user_count += 1 

    def __str__(self): ###i am using the string method to print
        print(f"Hello {self.username}, your email is {self.email}")


user1= User("James Okodei", "Jamesok99@gmail.com")
user2= User("Sally Emma", "Salem22@gmail.com")

print(User.user_count)
print(user1.user_count)
print(user2.user_count)


## Static Methods vs Instance Methods 


"""

- Static Methods belong to the class itself and do not belong to any other instance. We use @staticmethod decorator for that

- Instance methods belongs to the class

"""


##static method

class BankAccount:
    Min_Balance= 100

    def __init__(self, owner, balance=0 ):
        self.owner= owner
        self._balance= balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s new balance is: ${self._balance}")
        else:
            print("Deposit amount must be positve")

    @staticmethod ## this static method belongs to the class 
    def is_valid_interest_rate(rate):
            return 0 <= rate <= 5

account= BankAccount("Alice", 500)

account.deposit(400)

print(BankAccount.is_valid_interest_rate(4))
        


"""
It is important to note that we can also make methods protected or privatized 

"""

##protecting methods 

class BankAccount:
    Min_Balance= 100

    def __init__(self, owner, balance=0 ):
        self.owner= owner
        self._balance= balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__log_transaction("deposit", amount)
            print(f"{self.owner}'s new balance is: ${self._balance}")
        else:
            print("Deposit amount must be positve")

    def withdraw(self, amount): ##this is for withdrawing funds
        if amount < self._balance:
            self._balance -= amount
            self.__log_transaction("withdrawal", amount)
        else:
            print("You withdrawal is more than your balance ")
    
    def _is_valid_amount(self, amount): ##we created a protected amount 
        return amount > 0
    
    def __log_transaction(self, transaction_type, amount): ## this is a private class 
        print(f"Logging the {transaction_type} of ${amount}. New Balance is ${self._balance}")


    @staticmethod ## this static method belongs to the class 
    def is_valid_interest_rate(rate):
            return 0 <= rate <= 5

account= BankAccount("Alice", 500)

account.deposit(400)

account.withdraw(600)