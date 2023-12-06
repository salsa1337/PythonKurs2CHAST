import doctest
from typing import Union

class Furniture:
    def __init__(self, material: str, color: str, weight: Union[int, float]):
        """
        Создание объекта "Мебель".

        :param material: Материал, из которого изготовлена мебель.
        :param color: Цвет мебели.
        :param weight: Вес мебели в килограммах.

        Примеры:
        >>> chair = Furniture("дерево", "коричневый", 10)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        self.material = material

        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        self.color = color

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес мебели должен быть положительным числом")
        self.weight = weight

    def move_furniture(self, new_location: str) -> None:
        """
        Перемещение мебели в новое место.

        :param new_location: Новое местоположение мебели.

        Примеры:
        >>> chair = Furniture("дерево", "коричневый", 10)
        >>> chair.move_furniture("Гостиная")
        """
        ...

    def change_color(self, new_color: str) -> None:
        """
        Изменение цвета мебели.

        :param new_color: Новый цвет мебели.

        Примеры:
        >>> chair = Furniture("дерево", "коричневый", 10)
        >>> chair.change_color("белый")
        """
        ...


class Tree:
    def __init__(self, species: str, height: Union[int, float], age: int):
        """
        Создание объекта "Дерево".

        :param species: Вид дерева.
        :param height: Высота дерева в метрах.
        :param age: Возраст дерева в годах.

        Примеры:
        >>> oak_tree = Tree("дуб", 5.5, 20)
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой")
        self.species = species

        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height = height

        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным числом")
        self.age = age

    def grow(self, additional_height: Union[int, float]) -> None:
        """
        Увеличение высоты дерева.

        :param additional_height: Дополнительная высота, на которую вырастет дерево.

        Примеры:
        >>> oak_tree = Tree("дуб", 5.5, 20)
        >>> oak_tree.grow(0.5)
        """
        ...

    def shed_leaves(self) -> None:
        """
        Процесс сбрасывания листьев с дерева.

        Примеры:
        >>> oak_tree = Tree("дуб", 5.5, 20)
        >>> oak_tree.shed_leaves()
        """
        ...


class SocialMediaPlatform:
    def __init__(self, name: str, users: int, founded_year: int):
        """
        Создание объекта "Социальная сеть".

        :param name: Название социальной сети.
        :param users: Количество пользователей.
        :param founded_year: Год основания социальной сети.

        Примеры:
        >>> facebook = SocialMediaPlatform("Facebook", 2800000000, 2004)
        """
        if not isinstance(name, str):
            raise TypeError("Название социальной сети должно быть строкой")
        self.name = name

        if not isinstance(users, int):
            raise TypeError("Количество пользователей должно быть целым числом")
        if users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным числом")
        self.users = users

        if not isinstance(founded_year, int):
            raise TypeError("Год основания должен быть целым числом")
        if founded_year <= 0:
            raise ValueError("Год основания должен быть положительным числом")
        self.founded_year = founded_year

    def add_user(self) -> None:
        """
        Добавление нового пользователя в социальную сеть.

        Примеры:
        >>> facebook = SocialMediaPlatform("Facebook", 2800000000, 2004)
        >>> facebook.add_user()
        """
        ...

    def remove_user(self) -> None:
        """
        Удаление пользователя из социальной сети.

        Примеры:
        >>> facebook = SocialMediaPlatform("Facebook", 2800000000, 2004)
        >>> facebook.remove_user()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()

