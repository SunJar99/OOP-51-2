# The ((((@classmethod)))) decorator in Python is used to define a method that is bound to the class,
# rather than an instance of the class. This means that when you call a class method,
# it takes the class itself as its first argument, typically named cls.

# @classmethod allows the method to operate on the class itself and not on individual instances.
# It is used when you need to perform actions or computations related to the class
# rather than any particular instance of the class.
# You can access and modify class-level attributes inside a class method using the cls parameter.


# The ((((@staticmethod)))) decorator in Python is used to define a method that does not depend on the instance or the class itself.
# It works like a regular function but is placed inside the class for organizational purposes.

# It is useful when you need a utility function that logically belongs to the class
# but doesn’t need to access or modify class or instance attributes.
# It is more like a normal function but is kept inside the class for better organization.


# In Python, cls and self are used in different contexts, though both serve as references within a class.
# Here's the distinction:

# self:

# Refers to the instance of the class.
# It is used in instance methods to access or modify the instance's attributes and methods.
# Every instance method of a class has self as its first parameter, 
# which allows it to operate on the specific instance of the class.

# cls:

# Refers to the class itself.
# It is used in class methods, which are methods that operate on the class level, rather than on instances.
# Class methods are decorated with @classmethod, and the first argument is conventionally cls,
# which allows access to class attributes and other class methods.


def my_decorator(func):
    
    def wrapper():
        print('Before activating a function')
        func()
        print('After activating a function')
        
    return wrapper

@my_decorator
def hello():
    print('hello world')
    
hello()

def repeat(n):
    
    def decorator(func):
        
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print('Nice to meet you')

greet()


def class_decorators(cls):
    class NewClass(cls):
        
        def new_method(self):
            return print("something new")
        
    return NewClass

@class_decorators
class MyClass:
    
    def old_method(self):
        return print('old method')
    
obj = MyClass()
obj.old_method()
obj.new_method()


class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"some somes soem"
    
obj = Person("goof", 25)

print(obj)


class Money:
    
    def __init__(self, amount):
        self.amount = amount
        
    def __add__(self, other):
        return Money(self.amount + other.amount)
    
    def __str__(self):
        return f"{self.amount} som"
    
m1 = Money(100)
m2 = Money(200)
m3 = m2 + m1
print(m3)

class Math:
     
    def add(self, a, b):
        return a + b
    
obj3 = Math()

print(obj3.add(1,2))


class Person:
    count = 0
    password = "Def"
    
    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    @classmethod
    def get_population(cls):
        return cls.count
    
    
    def test(self):
        pass

    @classmethod
    def create_person(cls, name):
        return cls(name)

person1 = Person("Alice")
person2 = Person("ZHandar")
person3 = Person("Abaia")
print(Person.get_population())
person4 = Person.create_person("John")
print(person4.name)