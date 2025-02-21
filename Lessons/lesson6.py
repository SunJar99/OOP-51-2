


# # class Flyable:
    
# #     def fly(self):
# #         return 'flying'
    
    
# # class swimmable:
    
# #     def swim(self):
# #         return 'swimming'
    

# # class Duck(Flyable, swimmable):
    
# #     def make_sound(self):
# #         return 'Duck noises'
    
# # donald_duck = Duck()
# # print(donald_duck.fly())
# # print(donald_duck.swim())


# # Ромбовидное наследование

# class Animal:
    
#     def __init__(self, name):
#         self.name = name
    
#     def make_sound(self):
#         return "Makes sound"
    
# class Flyable(Animal):
    
#     def fly(self):
#         return 'flying'
    
    
# class swimmable(Animal):
    
#     def swim(self):
#         return 'swimming'
    
# class Duck(Flyable, swimmable):
    
#     def make_sound(self):
#         return 'Duck noises'
    
# donald_duck = Duck()
# print(donald_duck.fly())
# print(donald_duck.swim())






import sqlite3

# A4 paper
connect = sqlite3.connect('User.db')

# Hand with pen
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT 
    )           
               ''')

# Saving 
connect.commit()

# CRUD - Create - Read - Update - Delete

# Create
def add_user(name, age, hobby):
    
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )

    connect.commit()
    print(f"Пользователь {name} добавлен")

name = input("Name: ")
age = input("Age: ")
hobby = input("Hobby: ")
    
add_user(name, age, hobby)
# add_user("John", 33, "Swimming")
# add_user("Ardager", 25, "Sleeping")
# add_user("Zhandar", 17, "Winning")


def get_all_users():
    
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print(users)
    print("List of all users")
    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")
        

get_all_users()