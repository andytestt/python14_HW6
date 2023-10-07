import sqlite3
from faker import Faker
import random
import datetime

# Ініціалізуємо об'єкт Faker
fake = Faker()
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Підключаємося до бази даних (створюємо або відкриваємо існуючу)
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Створюємо таблицю студентів
cursor.execute('''CREATE TABLE IF NOT EXISTS students
                  (id INTEGER PRIMARY KEY,
                   first_name TEXT,
                   last_name TEXT,
                   group_id INTEGER)''')

# Створюємо таблицю груп
cursor.execute('''CREATE TABLE IF NOT EXISTS groups
                  (id INTEGER PRIMARY KEY,
                   name TEXT)''')

# Створюємо таблицю викладачів
cursor.execute('''CREATE TABLE IF NOT EXISTS professors
                  (id INTEGER PRIMARY KEY,
                   first_name TEXT,
                   last_name TEXT)''')

# Створюємо таблицю предметів
cursor.execute('''CREATE TABLE IF NOT EXISTS subjects
                  (id INTEGER PRIMARY KEY,
                   name TEXT,
                   professor_id INTEGER)''')

# Створюємо таблицю оцінок студентів
cursor.execute('''CREATE TABLE IF NOT EXISTS grades
                  (id INTEGER PRIMARY KEY,
                   student_id INTEGER,
                   subject_id INTEGER,
                   grade INTEGER,
                   date_taken DATE)''')

# Додаємо дані до таблиці груп
groups = ['Group A', 'Group B', 'Group C']
for group_name in groups:
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (group_name,))
    conn.commit()

# Додаємо дані до таблиці викладачів
for _ in range(5):
    first_name = fake.first_name()
    last_name = fake.last_name()
    cursor.execute("INSERT INTO professors (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
    conn.commit()

# Додаємо дані до таблиці предметів
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'English', 'Computer Science']
professor_ids = [1, 2, 3, 4, 5]  # Припускаємо, що у нас є 5 викладачів
for subject_name in subjects:
    professor_id = random.choice(professor_ids)
    cursor.execute("INSERT INTO subjects (name, professor_id) VALUES (?, ?)", (subject_name, professor_id))
    conn.commit()

# Додаємо дані до таблиці студентів та оцінок
num_students = random.randint(30, 50)
for _ in range(num_students):
    first_name = fake.first_name()
    last_name = fake.last_name()
    group_id = random.randint(1, 3)
    cursor.execute("INSERT INTO students (first_name, last_name, group_id) VALUES (?, ?, ?)", (first_name, last_name, group_id))
    student_id = cursor.lastrowid

    # Додаємо оцінки для студента
    for subject_id in range(1, random.randint(5, 8) + 1):
        grade = random.randint(60, 100)
        date_taken = fake.date_between(start_date='-1y', end_date='today')
        cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date_taken) VALUES (?, ?, ?, ?)",
                       (student_id, subject_id, grade, date_taken))
    conn.commit()

# Закриваємо з'єднання з базою даних
conn.close()

print("База даних створена і заповнена випадковими даними.")

