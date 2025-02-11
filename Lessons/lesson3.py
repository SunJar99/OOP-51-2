# The @abstractmethod decorator in Python is used to declare abstract methods in an abstract base class (ABC).
# An abstract method is a method that is declared in a base class but does not have any implementation.
# Subclasses of the abstract base class are required to provide their own implementation of the abstract method.

# A class containing one or more abstract methods cannot be instantiated directly.
# Subclasses that inherit from the abstract base class must implement all abstract methods in order to be instantiated.
# Abstract methods are often used when you want to define a common interface for all subclasses,
# but leave the specific implementation details to the subclasses.

from abc import ABC, abstractmethod
# Abstract basic class

class  OTPSrvice(ABC):
    
    @abstractmethod
    def sms_send(self):
        pass
    
    
class ZhandarOTP(OTPSrvice):
    
    
    def sms_send(self, phone):
        phone = input('Do something')
        
        
        
class AbaiOTP(OTPSrvice):
    
    def sms_send(self, phone):
        phone = input('Do something something')
        
        
        

class Animal(ABC):
    
    #Decorator @abstractmethod
    @abstractmethod 
    def makeSound(self):
        pass
    
    @abstractmethod
    def move(self):
        self
        
class Dog(Animal):
    
    def makeSound(self):
        return print('Gaf gaf')
    
    def move(self):
        return print('run')

# dog = Dog()
# dog.makeSound()




from colorama import init, Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'some green text')
print(Style.DIM  + 'some dim text')
print(Style.RESET_ALL)
print('Back to normal now')

from django.db import models
from django.urls import path

test = models.BigIntegerField(auto_created=True)
test2 = path()