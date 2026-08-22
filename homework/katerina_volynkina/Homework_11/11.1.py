class Book:
    material_pages = "бумага"
    text_present = "есть"
    reserved = False
    ISBN = None

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}'
                f'{", зарезервирована" if self.reserved else ""}')


class TextBook(Book):
    def __init__(self, title, author, pages, subject, school_class, has_tasks=False):
        super().__init__(title, author, pages)
        self.subject = subject
        self.school_class = school_class
        self.has_tasks = has_tasks

    def __str__(self):
        return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, '
                f'предмет: {self.subject}, класс {self.school_class}'
                f'{", зарезервирована" if self.reserved else ""}')


book_1 = Book("Идиот", "Достоевский", "500")
book_1.reserved = True
book_2 = Book("Война и мир первый том", "Толстой", "850")
book_3 = Book("Война и мир второй том", "Достоевский", "600")
book_4 = Book("Война и мир третий том", "Достоевский", "1100")
book_5 = Book("Война и мир четвертый том", "Достоевский", "785")

all_books = [book_1, book_2, book_3, book_4, book_5]
for book in all_books:
    print(book)

textbook_1 = TextBook("Алгебра", "Перельман", "200", "Математика", "9")
textbook_2 = TextBook("Геометрия", "Перельман", "500", "Математика", "9")
textbook_3 = TextBook("Русская литература", "Петров", "250", "Литература", "9")
textbook_3.reserved = True
textbook_4 = TextBook("Средние века", "Иванов", "850", "История", "9")

all_textbooks = [textbook_1, textbook_2, textbook_3, textbook_4]
for textbook in all_textbooks:
    print(textbook)
