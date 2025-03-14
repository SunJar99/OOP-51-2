import random
class Heroes:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk
        
    def attack(self):
        print(f"{self.name} attacks!, dealt {self.atk} of damage!")
    
    def status(self):
        print(f"{self.name}, {self.hp}HP, {self.atk}ATK")
        
    
class Warrior(Heroes):
    
    def __init__(self, name, hp, atk, buff):
        super().__init__(name, hp, atk)
        self.buff = buff
        
    def action(self):
        print(f"{self.name} attacking twice! {self.atk + self.atk} was dealt!")
    
    def powerup(self):
        self.atk = self.atk + self.buff
        print(f"{self.name} has used ATK UP! ATK has been increased up to {self.atk} for 2 turns!")
    
    

class Archer(Heroes):
    
    def __init__(self, name, hp, atk, arrows, precision):
        super().__init__(name, hp, atk)
        self.arrows = arrows
        self.precision = precision
        
    def attack(self):
        self.arrows -= 1
        gamble = random.randrange(1, 100)
        if self.precision >= gamble:
            print(f"{self.name} used an arrow to attack! Looks like bullseye! Hit for {self.atk}, {self.arrows} left!")
        else:
            print(f"{self.name} used an arrow to attack! Looks like {self.name} missed... {self.arrows} left.")
    
    def action(self):
        precisionIncrease = random.randrange(1, 50)
        self.precision = self.precision + precisionIncrease
        print(f"{self.name} is focusing... increased precision up to {self.precision} for next attack!")
            
    def rest(self):
        self.arrows += 5
        print(f"{self.name} has gained 5 arrows back! {self.arrows} remaining now!")
    
    def status(self):
        print(f"{self.name}, {self.hp}HP, {self.atk}ATK, {self.arrows} arrows, {self.precision}% Precision")

zhandar = Archer(name="Zhandar", hp=150, atk=100, arrows=5, precision=70)
abai = Warrior(name="Abai", hp=350, atk=100, buff=100)

zhandar.action()
abai.action()

zhandar.attack()
abai.attack()

abai.powerup()

zhandar.rest()

zhandar.status()
abai.status()