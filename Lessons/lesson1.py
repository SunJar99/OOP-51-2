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
        self.name = name
        self.hp = hp
        self.lvl = lvl
    
    def action(self):
        print(f"{self.name} Doing base actions.")
        
    def introduce(self):
        print(f"Hello, my name is {self.name}, I'm level {self.lvl}, have {self.hp} of hp.")
    
    def lvl_10(self):
        if self.lvl >= 10:
            print(True)
        else:
            print(False)

# Naofumi = Hero("NaoFumi", 200, 15)


class ShieldHero(Hero):
    
    def __init__(self, name, hp, lvl, barrier):
        super().__init__(name, hp, lvl)
        self.barrier = barrier
        
    def defenseSkill(self):
        print(f"{self.name} uses BarrierUp! {self.barrier} of barrier gained!")
        
class SpearHero(Hero):
    
    def __init__(self, name, hp, lvl, precision):
        super().__init__(name, hp, lvl)
        self.precision = precision
    
    def spearSkill(self):
        print(f"{self.name} used special skill 'Precision'!, +{self.precision}% crit rate gained!")

class Warrior(Hero):
    
    def __init__(self, name, hp, lvl, st):
        super().__init__(name, hp, lvl)
        self.st = st
    
    def warriorAction(self):
        print(f"{self.name} doing actions")
# Write the difference between ... and pass
# Both of these functions work almost the same but ... is a bit more complicated than "pass",
# since "pass" is just for placeholder which doesnt do anything, "..." is an actual expression since it has type of "Ellipsis"
# For example we can print(...) while we cant print(pass)

naofumi = ShieldHero("NaoFumi", 200, 15, 50)
kitamura = SpearHero("Kitamura", 115, 16, 20)
# You can write values in any order if named: 
kirrito = Warrior(lvl=5, hp=50, st=50, name='Kirrito')

naofumi.introduce()
kitamura.introduce()
kirrito.introduce()

naofumi.lvl_10()
kitamura.lvl_10()
kirrito.lvl_10()

naofumi.action()
kitamura.action()
kirrito.action()

naofumi.defenseSkill()
kitamura.spearSkill()
kirrito.warriorAction()
# class --CamelCase
# object for functions --snek_case


