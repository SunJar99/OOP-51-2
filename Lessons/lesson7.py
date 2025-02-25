import sqlite3

# A4 paper
connect = sqlite3.connect('User.db')

# Hand with pen
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT 
    )           
               ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        subject VARCHAR (50) NOT NULL,
        grade INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
                ''')
connect.commit()


def add_user(name, age, hobby):
    
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )

    connect.commit()
    print(f"Пользователь {name} добавлен")

# name = input("Name: ")
# age = input("Age: ")
# hobby = input("Hobby: ")
    
# add_user(name, age, hobby)
# add_user("John", 33, "Swimming")
# add_user("Ardager", 25, "Sleeping")
# add_user("Zhandar", 17, "Winning")


def add_grade(user_id, subject, grade):
    cursor.execute('''
        INSERT INTO grades (user_id, subject, grade) VALUES (?,?,?)
                ''',
                (user_id, subject, grade))
    connect.commit()
    print(f'Graded the person with id of {user_id}!!!')

# add_grade(4, "Algebra", 5)
# add_grade(3, "Algebra", 5)
# add_grade(2, "Algebra", 5)
# add_grade(1, "Algebra", 5)
# add_grade(4, "Draw", 5)
# add_grade(3, "Draw", 5) 
# add_grade(2, "Draw", 5)
# add_grade(1, "Draw" , 5)


def update_grade(new_grade, user_id, id):
    cursor.execute(
        'UPDATE grades SET grade = ? WHERE user_id = ? AND subject = ?',
        (new_grade, user_id, id)
    )
    
    connect.commit()
    print(f'subject {id} updated !!')

update_grade(new_grade=4, user_id=1, id="Algebra")

def get_users_with_grades():
    cursor.execute('''
        SELECT users.name, grades.subject, grades.grade
        FROM users
        LEFT JOIN grades ON users.user_id = grades.user_id
                   ''')
    
    users = cursor.fetchall()
    for i in users:
        print(f"NAME: {i[0]}, SUBJECT: {i[1]}, GRADE: {i[2]}")
        
get_users_with_grades()
