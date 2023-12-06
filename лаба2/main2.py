class Library:
    def __init__(self, books=None):
        """
        Инициализация объекта Library.

        :param books: Список книг. Если не передан, инициализируется пустым списком.
        """
        self.books = books or []

    def get_next_book_id(self) -> int:
        """
        Метод возвращает идентификатор для добавления новой книги в библиотеку.

        :return: Идентификатор для новой книги.
        """
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Метод возвращает индекс книги в списке библиотеки по её идентификатору.

        :param book_id: Идентификатор книги.
        :return: Индекс книги в списке библиотеки.
        :raise ValueError: Если книги с запрашиваемым id не существует.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError(f"Книги с id={book_id} не существует")


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация объекта Book.

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __repr__(self) -> str:
        """
        Метод для представления объекта в виде валидной строки Python.

        :return: Строка, по которой можно инициализировать точно такой же экземпляр.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


# Тестирование класса Library
BOOKS_DATABASE = [
    {"id": 1, "name": "test_name_1", "pages": 200},
    {"id": 2, "name": "test_name_2", "pages": 400}
]

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
