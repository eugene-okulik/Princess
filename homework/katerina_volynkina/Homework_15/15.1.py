import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)


cursor = db.cursor(dictionary=True, buffered=True)
cursor.execute("INSERT INTO students (name, second_name) VALUES ('Василиса', 'Васильева')")
student_id = cursor.lastrowid
cursor.execute("SELECT * FROM students ORDER BY id DESC LIMIT 1")
data = cursor.fetchall()
print(data)

cursor.execute(f"INSERT INTO books (title, taken_by_student_id) VALUES ('Universe The Definitive visual guid', {student_id})")
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) VALUES ('Death on the Nile', {student_id})")
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) VALUES ('Выдающиеся растения, которые изменили нашу жизнь', {student_id})")
cursor.execute(f"SELECT * FROM books WHERE taken_by_student_id = {student_id}")
data_1 = cursor.fetchall()
print(data_1)

cursor.execute("INSERT INTO `groups`(title, start_date, end_date) VALUES ('Всё обо всём', 'september 2026', 'december 2026')")
groups_id_1 = cursor.lastrowid
cursor.execute(f"SELECT * FROM `groups` where title = 'Всё обо всём' and id = {groups_id_1}")# 25076
data_2 = cursor.fetchone()
print(data_2)
cursor.execute(f"UPDATE students SET group_id = {groups_id_1} where id = {student_id}")
cursor.execute("SELECT * FROM students ORDER BY id DESC LIMIT 1")
print(cursor.fetchall())

cursor.execute("INSERT INTO subjects (title) VALUES ('Фитнес как психология')")
subjects_id_1 = cursor.lastrowid
cursor.execute(f"SELECT * FROM subjects where title = 'Фитнес как психология' and id = {subjects_id_1}")
data_3 = cursor.fetchall()
print(data_3)
cursor.execute("INSERT INTO subjects (title) VALUES ('Спортивная физиология')")
subjects_id_2 = cursor.lastrowid
cursor.execute(f"SELECT * FROM subjects where title = 'Спортивная физиология' and id = {subjects_id_2}")
data_4 = cursor.fetchone()
print(data_4)
cursor.execute("INSERT INTO subjects (title) VALUES ('Анатомия')")
subjects_id_3 = cursor.lastrowid
cursor.execute(f"SELECT * FROM subjects where title = 'Анатомия' and id = {subjects_id_3}")
data_5 = cursor.fetchone()
print(data_5)

cursor.execute(f"SELECT * FROM subjects where id = {subjects_id_1} or id = {subjects_id_2} or id = {subjects_id_3}")
print(cursor.fetchall())

cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Психология', {subjects_id_1})")
lessons_id_1 = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Биомеханика', {subjects_id_1})")
lessons_id_2 = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Эндокринология', {subjects_id_2})")
lessons_id_3 = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('МФР', {subjects_id_2})")
lessons_id_4 = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Анатомия человека', {subjects_id_3})")
lessons_id_5 = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Физиология', {subjects_id_3})")
lessons_id_6 = cursor.lastrowid

cursor.execute("SELECT * FROM lessons ORDER BY id DESC LIMIT 6")
data_6 = cursor.fetchall()
print(data_6)

cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', {lessons_id_1}, {student_id})")
cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('2', {lessons_id_2}, {student_id})")
cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('3', {lessons_id_3}, {student_id})")
cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('4', {lessons_id_4}, {student_id})")
cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('2', {lessons_id_5}, {student_id})")
cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', {lessons_id_6}, {student_id})")

cursor.execute("SELECT * FROM marks ORDER BY id DESC LIMIT 6")
data_7 = cursor.fetchall()
print(data_7)

cursor.execute(f"SELECT value FROM marks where student_id = {student_id}")
data_8 = cursor.fetchall()
print(f"Оценки студента {data_8}")

cursor.execute(f"SELECT title FROM books where taken_by_student_id = {student_id}")
data_9 = cursor.fetchall()
print(f"Книги, которые взял студент {data_9}")

cursor.execute(f'''SELECT s.id, s.name Имя, s.second_name Фамилия, g.title Группа,
       su.title Предмет, l.title Урок, m.value Оценка , b.title Книга
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects su ON l.subject_id = su.id
WHERE s.id = {student_id}''')

data_10 = cursor.fetchall()
print(data_10)


db.commit()

db.close()