import mysql.connector as mysql
import os
import csv
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_DATABASE')
)

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
princess_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

cursor = db.cursor(dictionary=True, buffered=True)
with open(princess_path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    data = []
    for row in file_data:
        data.append(row)
for row in data:
    name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row
    query = '''SELECT s.id, s.name Имя, s.second_name Фамилия, g.title Группа,
           su.title Предмет, l.title Урок, m.value Оценка , b.title Книга
    FROM students s
    LEFT JOIN `groups` g ON s.group_id = g.id
    LEFT JOIN books b ON s.id = b.taken_by_student_id
    LEFT JOIN marks m ON s.id = m.student_id
    LEFT JOIN lessons l ON m.lesson_id = l.id
    LEFT JOIN subjects su ON l.subject_id = su.id
    WHERE s.name = %s AND s.second_name = %s'''
    cursor.execute(query, (name, second_name))
    student = cursor.fetchone()

    if student:
        print(student)
    else:
        print(f'Нет в БД: {student}')

cursor.close()
db.close()
