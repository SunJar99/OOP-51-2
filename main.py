# class Person:
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def introduce(self):
#         print(f"Hi Im {self.name}")
        
        
        
# something = Person("Ardager", 25)

# something.introduce()

# print(type(something))
# print(type(123))
# print(type("Hello"))

class Hero:
    
    def __init__(self, name, hp, lvl):
        self.name_1 = name
        self.hp_1 = hp
        self.lvl_1 = lvl
    
    def action(self):
        print(f"{self.name_1} Doing base actions.")

# Naofumi = Hero("NaoFumi", 200, 15)


class ShieldHero(Hero):
    pass

# Write the difference between ... and pass
# Both of these functions work almost the same but ... is a bit more complicated than "pass",
# since "pass" is just for placeholder which doesnt do anything, "..." is an actual expression since it has type of "Ellipsis"
# For example we can print(...) while we cant print(pass)

naofumi = Hero("NaoFumi", 200, 15)

naofumi.action()

# class --CamelCase
# object for functions --snek_case


