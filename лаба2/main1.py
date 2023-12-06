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

    def __str__(self) -> str:
        """
        Метод для представления объекта в виде строки.

        :return: Строка формата "Книга 'название_книги'".
        """
        return f"Книга \"{self.name}\""

    def __repr__(self) -> str:
        """
        Метод для представления объекта в виде валидной строки Python.

        :return: Строка, по которой можно инициализировать точно такой же экземпляр.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


# Тестирование класса Book
BOOKS_DATABASE = [
    {"id": 1, "name": "test_name_1", "pages": 200},
    {"id": 2, "name": "test_name_2", "pages": 400}
]

if __name__ == '__main__':
    # Инициализация списка книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    # Проверка метода __str__
    for book in list_books:
        print(book)

    # Проверка метода __repr__
    print(list_books)
