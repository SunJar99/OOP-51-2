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

# name = input("Name: ")

# if name == "No":
#     print("Nothing will be added.")
# else:
#     age = input("Age: ")
#     hobby = input("Hobby: ")
#     add_user(name, age, hobby)


def get_user_by_name(name):
    
    cursor.execute(f'SELECT * FROM users WHERE name = ?', (name,))
    users = cursor.fetchall()
    for i in users:
        return f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}"
    
    
print(get_user_by_name("Zhandar"))

# add_user("John", 33, "Swimming")
# add_user("Ardager", 25, "Sleeping")
# add_user("Zhandar", 17, "Winning")


# def get_all_users():
    
#     cursor.execute('SELECT * FROM users')
#     users = cursor.fetchall()
#     print(users)
#     print("List of all users")
#     for i in users:
#         print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")
        

# get_all_users()