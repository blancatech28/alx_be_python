class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out_book(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_checked_out(self):
        return self._is_checked_out



class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.is_checked_out():
                    book.check_out_book()
                return

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.is_checked_out():
                    book.return_book()
                return

    def list_available_books(self):
        for book in self._books:
            if not book.is_checked_out():
                print(f"{book.title} by {book.author}")
