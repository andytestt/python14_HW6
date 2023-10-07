import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Виконання запиту з файлу query_1.sql
with open('query_2.sql', 'r') as query_file:
    sql_query = query_file.read()
    cursor.execute(sql_query)

# Отримання результатів запиту
results = cursor.fetchall()

# Виведення результатів
for row in results:
    print(row)

# Закриття з'єднання з базою даних
conn.close()