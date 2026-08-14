class Book:
    material_pages = "бумага"
    text_present = "есть"
    def __init__(self, title, author, pages, reserved = False, ISBN = None):
        self.title = title
        self.author = author
        self.pages = pages
        self.reserved = reserved
        self.ISBN = ISBN



class TextBook(Book):
    def __init__(self, title, author, pages, subject, school_class, has_tasks = False, ISBN = None):
        super().__init__(title, author, pages, ISBN = ISBN)
        self.subject = subject
        self.school_class = school_class
        self.has_tasks = has_tasks


book_1 = Book("Идиот", "Достоевский", "500", True)
book_2 = Book("Война и мир первый том", "Толстой", "850")
book_3 = Book("Война и мир второй том", "Достоевский", "600")
book_4 = Book("Война и мир третий том", "Достоевский", "1100")
book_5 = Book("Война и мир четвертый том", "Достоевский", "785")


print(f'Название: {book_1.title}, Автор: {book_1.author}, страниц: {book_1.pages}, '
      f'материал: {book_1.material_pages}'
      f'{", зарезервирована" if book_1.reserved else ""}')
print(f'Название: {book_2.title}, Автор: {book_2.author}, страниц: {book_2.pages}, '
      f'материал: {book_2.material_pages}'
      f'{", зарезервирована" if book_2.reserved else ""}')
print(f'Название: {book_3.title}, Автор: {book_3.author}, страниц: {book_3.pages}, '
      f'материал: {book_3.material_pages}'
      f'{", зарезервирована" if book_3.reserved else ""}')
print(f'Название: {book_4.title}, Автор: {book_4.author}, страниц: {book_4.pages}, '
      f'материал: {book_4.material_pages}'
      f'{", зарезервирована" if book_4.reserved else ""}')
print(f'Название: {book_5.title}, Автор: {book_5.author}, страниц: {book_5.pages}, '
      f'материал: {book_5.material_pages}'
      f'{", зарезервирована" if book_4.reserved else ""}')


textbook_1 = TextBook("Алгебра", "Перельман", "200", "Математика", "9")
textbook_2 = TextBook("Геометрия", "Перельман", "500", "Математика", "9")
textbook_3 = TextBook("Русская литература", "Петров", "250", "Литература", "9", True)
textbook_4 = TextBook("Средние века", "Иванов", "850", "История", "9")


print(f'Название: {textbook_1.title}, Автор: {textbook_1.author}, страниц: {textbook_1.pages}, '
      f'предмет: {textbook_1.subject}, класс {textbook_1.school_class}'
      f'{", зарезервирована" if textbook_1.has_tasks else ""}')
print(f'Название: {textbook_2.title}, Автор: {textbook_2.author}, страниц: {textbook_2.pages}, '
      f'предмет: {textbook_2.subject}, класс {textbook_2.school_class}'
      f'{", зарезервирована" if textbook_2.has_tasks else ""}')
print(f'Название: {textbook_3.title}, Автор: {textbook_3.author}, страниц: {textbook_3.pages}, '
      f'предмет: {textbook_3.subject}, класс {textbook_3.school_class}'
      f'{", зарезервирована" if textbook_3.has_tasks else ""}')
print(f'Название: {textbook_4.title}, Автор: {textbook_4.author}, страниц: {textbook_4.pages}, '
      f'предмет: {textbook_4.subject}, класс {textbook_4.school_class}'
      f'{", зарезервирована" if textbook_4.has_tasks else ""}')
