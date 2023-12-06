class Animal:
    """
    Базовый класс для представления животных.
    """

    def __init__(self, species: str, habitat: str):
        """
        Инициализация объекта Animal.

        :param species: Вид животного.
        :param habitat: Место обитания животного.
        """
        self._species = species
        self._habitat = habitat

    def move(self):
        """
        Метод, представляющий движение животного.

        :return: Описание движения животного.
        """
        return f"The {self._species} is moving."


class Bird(Animal):
    """
    Дочерний класс, представляющий птиц.
    """

    def __init__(self, species: str, habitat: str, wingspan: float):
        """
        Инициализация объекта Bird.

        :param species: Вид птицы.
        :param habitat: Место обитания птицы.
        :param wingspan: Размах крыльев птицы в метрах.
        """
        super().__init__(species, habitat)
        self._wingspan = wingspan

    def fly(self):
        """
        Перегруженный метод для представления полета птицы.

        :return: Описание полета птицы.
        """
        return f"The {self._species} is flying with a wingspan of {self._wingspan} meters."


if __name__ == "__main__":
    # Пример использования классов

    lion = Animal(species="Lion", habitat="Savannah")
    print(lion.move())  # Пример вызова унаследованного метода

    eagle = Bird(species="Eagle", habitat="Mountains", wingspan=2.0)
    print(eagle.move())  # Пример вызова унаследованного метода
    print(eagle.fly())  # Пример вызова перегруженного метода
