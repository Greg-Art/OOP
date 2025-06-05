"""

-This chapter will focus mainly on how we can access attributes and object data and how we can:

- Modify
- Protect
- Privatize some attributes 
- Using Getters and Setters 

"""

# Accessing other class values 
##creating a class user 

class User:
    def __init__(self, username, email, password):
        self.username= username
        self.email= email 
        self.password= password
    
    def say_hi_to_user(self, user): ##with this we are passing self to allow us access all the above attributes and the allow a new argument (user) to be requested and used by the method
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}")


##creating some new objects of our class User
user1= User("GregoryArt", "gart98@gmail.com", "GGHH44553")

user2= User("JamesAddison", "JAD99@gmail.com", "GGKJ4553")

user3= User("AliceSimmon", "Asim@gmail.com", "WKKJ4598*")

## we can send a message to another user
## in this case, user1 is sending a message to user2
user1.say_hi_to_user(user2)

##Modifying A Object Data
##we can modify the data of an object
user1.email= "gregart22@gmail.com"

user1.email

"""
With the above, we can see that this is a bad thing to do as we do not want people chaning passwords or emails easily 

This is where we can protect some attributes 

"""

## in this example, I am going to make password protected 

## to do this, I will use an underscore

class User:
    def __init__(self, username, email, password):
        self.username= username
        self.email= email 
        self._password= password ##added an underscore here to protect the password class this will prevent us from using it outside the class
    
    def say_hi_to_user(self, user): ##with this we are passing self to allow us access all the above attributes and the allow a new argument (user) to be requested and used by the method
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}")

    
    def get_password(self): ##here we are creating a method to allow us access the password within the class this is a getter 
        return self._password
    
    

    user3= User("James", "James123@gmail", "679282jjh")

    user3.password

    user3.password= "William233" ##trying to assign the email a new variable

    print(user3.password)


"""from this, we can see that:

- We cannot access the password attribute
- We cannot alsochange it's value
- That being said, you can access it outside the object if you refer to it with the single underscore (_) """


 ## Modifying inputs 

class User:
    def __init__(self, username, email, password):
        self.username= username
        self._email= email ##here we are protecting the email class
        self._password= password 
    def say_hi_to_user(self, user): ##with this we are passing self to allow us access all the above attributes and the allow a new argument (user) to be requested and used by the method
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}")

    
    def get_password(self): ##here we are creating a method to allow us access the password within the class this is a getter 
        return self._password
    
    def clean_email(self):
        return self._email.strip().lower().replace(" ", "") ## basically we are ensuring our class can accept email and automatically clean it up (remove all spaces and accept capitalized form) as it comes in 
    


    user5= User("JamesKotei", "JAMESKKT98@YAHOOMAIL.com", "998yhuKKHT8")

    user6= User("Kwame okoto", "Kwame Jokoto 98@gmail.com", "998yhuKKHT8")

    user7= User("Kwame okoto", "KwameJokoto98@gmail.com ", "998yhuKKHT8")
    
    print(user5.clean_email()) ## here we are seeing if our method can clean the capitalization
    print(user6.clean_email()) ## here is to deal with the spaces in between 
    print(user7.clean_email()) ## this is to handle the spaces at the end 


## Making Attributes private 

class User:
    def __init__(self, username, email, password):
        self.username= username
        self.__email= email ##here we are making the email attribute private, and we cannot access it outside the class at all
        self._password= password 
    def say_hi_to_user(self, user): ##with this we are passing self to allow us access all the above attributes and the allow a new argument (user) to be requested and used by the method
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}")

    
    def get_password(self): ##here we are creating a method to allow us access the password within the class this is a getter 
        return self._password
    
    def clean_email(self):
        return self.__email.strip().lower().replace(" ", "")
    
    user8= User("JameAkofio", "Jamesakof3344@gmail.com", "998jhaha09")

    print(user8.__email)

    ##however, we can access it with user8._User__email 


    ## Summary

"""

We have the following type of attributes

- Public: These are attributes with no protection and can be accessed outside the class 

- Protected: These are preceeded with an underscore before the attribute name. Not allowed to be accessed outside the class but can be accessed with the same format when calling the attribute

- Private: These are prefixed with a double underscore these are strictly prohibited. They cannot be accessed outside the class with the double underscore alone unless you specify the class prefixed by an underscore.

Generally we want to user protected variables 
"""

##Getters and Setters 

##even though we have seen a getter before, we will be revisiting them agian 

##Getter: This allows us to use protected and private attributes inside and outside a class 

class BankAccount:

    def __init__(self, name, email, password, balance):
        self.name= name
        self.email= email
        self.__password= password ##privitizing the password 
        self._balance= balance ##protecthing the balance 

    def get_balance(self): ##creating a getter to allow me use the balance inside and out  
        return self._balance 

    def get_password(self): ##creating a getter method 
        return self.__password
    
    def set_balance(self, new_balance): ##creating a setter method 
        self._balance = new_balance

    def set_password(self, new_password): ##creating a setter method 
        self.__password = new_password
    

##we will try to access them outside please note that this isn't recommended 

user_bank_act_1= BankAccount("Kwame Adams", "kadams998@yahoo.com", "JJ6YpgT$", "$12,344,887")

print(user_bank_act_1.get_balance()) ##we are trying to access the balance with the getter method
print(user_bank_act_1.get_password()) ##we are trying to access the password with the getter method

## Pleate Note: This Isn't A Good Practice in Python

##setting the new values 

user_bank_act_1.set_balance("$1233333") 
user_bank_act_1.set_password("Jk98YYtz0")

print(user_bank_act_1.get_balance())
print(user_bank_act_1.get_password())


"""

- We use getters and setters to allow us add more flexibility to see when a protected or privatized attribute was accessed 

- - For example, if someone on the team accesses or modifies a private/protected attribute directly (e.g., without using a setter), we lose control and visibility.

- But by using getters and setters, we can:
    - Track when the attribute was accessed or changed
    - Validate or sanitize new values
    - Log access/modification times or events
    - Prevent unauthorized or invalid updates

- This is useful in collaborative or sensitive systems where direct access could lead to bugs or security issues.

"""

##example below 

from datetime import datetime


class BankAccount:

    def __init__(self, name, email, password, balance):
        self.name= name
        self.email= email
        self.__password= password ##privitizing the password 
        self._balance= balance ##protecthing the balance 

    def get_balance(self): ##creating a getter to allow me use the balance inside and out  

        print(f"The balance was accessed at {datetime.now()}") ##have this log the time the balance
        return self._balance 

    def get_password(self): ##creating a getter method 
        print(f"The password was accessed at {datetime.now()}") ##have this log the time the balance
        return self.__password
    
    def set_balance(self, new_balance): ##creating a setter method 
        if "$" not in new_balance:
            raise ValueError("Input The Right Currency Symbol")   ##I am using the setter method to ensure that the user specifically inputs a dollar symbol when inputting their balance 
        self._balance = new_balance
            

    def set_password(self, new_password): ##creating a setter method 
        self.__password = new_password

user_bank_act_2= BankAccount("Kwame James", "kjames998@yahoo.com", "TT6YpgT$", "$77,344,887")


print(user_bank_act_2.get_balance())
print(user_bank_act_2.get_password())

