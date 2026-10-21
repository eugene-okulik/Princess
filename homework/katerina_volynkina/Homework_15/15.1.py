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

query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"

data = [
    ('Universe The Definitive visual guid', student_id),
    ('Death on the Nile', student_id),
    ('Выдающиеся растения, которые изменили нашу жизнь', student_id)
]

cursor.executemany(query, data)

query = "SELECT * FROM books WHERE taken_by_student_id = %s"
cursor.execute(query, (student_id,))
data_1 = cursor.fetchall()
print(data_1)

cursor.execute("INSERT INTO `groups`(title, start_date, end_date) "
               "VALUES ('Всё обо всём', 'september 2026', 'december 2026')")
groups_id_1 = cursor.lastrowid
query = "SELECT * FROM `groups` where title = 'Всё обо всём' and id = %s"
cursor.execute(query, (groups_id_1,))
data_2 = cursor.fetchone()
print(data_2)
query = "UPDATE students SET group_id = %s where id = %s"
cursor.execute(query, (groups_id_1,student_id))
cursor.execute("SELECT * FROM students ORDER BY id DESC LIMIT 1")
print(cursor.fetchall())

subjects = ['Фитнес как психология', 'Спортивная физиология', 'Анатомия']
ids = []
all = []
for name in subjects:
    query = "INSERT INTO subjects (title) VALUES (%s)"
    cursor.execute(query, [name])
    subjects_id = cursor.lastrowid
    ids.append(subjects_id)
    query = "SELECT * FROM subjects where title = %s and id = %s"
    cursor.execute(query, (name, subjects_id))
    data = cursor.fetchall()
    all.append(data)
print(all)
subjects_id_1, subjects_id_2, subjects_id_3= ids
query = "SELECT * FROM subjects where id = %s or id = %s or id = %s"
cursor.execute(query, (subjects_id_1, subjects_id_2, subjects_id_3))
print(cursor.fetchall())

lessons = ['Психология', 'Биомеханика', 'Эндокринология', 'МФР', 'Анатомия человека','Физиология']
subjects_id_1, subjects_id_2, subjects_id_3= ids
lessons_and_subjects = [
    ('Психология', subjects_id_1),
    ('Биомеханика', subjects_id_1),
    ('Эндокринология', subjects_id_2),
    ('МФР', subjects_id_2),
    ('Анатомия человека', subjects_id_3),
    ('Физиология', subjects_id_3)]
idL = []
allL = []
for name, subject_id in lessons_and_subjects:
    query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
    cursor.execute(query, (name, subject_id))
    lessons_id = cursor.lastrowid
    idL.append(lessons_id)
cursor.execute("SELECT * FROM lessons ORDER BY id DESC LIMIT 6")
data_6 = cursor.fetchall()
print(data_6)

lessons_id_1, lessons_id_2, lessons_id_3, lessons_id_4, lessons_id_5, lessons_id_6 = idL
query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
data = [
    ('5', lessons_id_1,student_id),
    ('2', lessons_id_2,student_id),
    ('3', lessons_id_3,student_id),
    ('4', lessons_id_4,student_id),
    ('2', lessons_id_5,student_id),
    ('5', lessons_id_6,student_id)
]
cursor.executemany(query, data)


cursor.execute("SELECT * FROM marks ORDER BY id DESC LIMIT 6")
data_7 = cursor.fetchall()
print(data_7)

query = "SELECT value FROM marks where student_id = %s"
cursor.execute(query, (student_id, ))
data_8 = cursor.fetchall()
print(f"Оценки студента {data_8}")

query = "SELECT title FROM books where taken_by_student_id = %s"
cursor.execute(query, (student_id, ))
data_9 = cursor.fetchall()
print(f"Книги, которые взял студент {data_9}")


query = '''SELECT s.id, s.name Имя, s.second_name Фамилия, g.title Группа,
       su.title Предмет, l.title Урок, m.value Оценка , b.title Книга
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects su ON l.subject_id = su.id
WHERE s.id = %s'''

cursor.execute(query, (student_id, ))
data_10 = cursor.fetchall()
print(data_10)


db.commit()

db.close()
