from Model.Characters import Magician, Priest
from random import randint


def get_hero_types_info():
    """Описание индивидуальных характеристик отдельных типов персонажей"""
    print(f"Magician: damageIndex = {Magician.Magician.damage_index}, protectIndex = {Magician.Magician.protect_index},"
          f" healIndex = {Magician.Magician.heal_index}")
    print(f"Priest: damageIndex = {Priest.Priest.damage_index}, protectIndex = {Priest.Priest.protect_index},"
          f" healIndex = {Priest.Priest.heal_index}")


def choose_hero_name():
    """Метод выбора (указания) имени создаваемого персонажа"""
    return input("Choose your HeroName: ")


def create_new_magician():
    """Метод создания нового персонажа класса "Маг"."""
    return Magician.Magician(choose_hero_name())


def create_new_priest():
    """Метод создания нового персонажа класса "Жрец"."""
    return Priest.Priest(choose_hero_name())


def create_new_hero():
    """Метод создания нового персонажа выбранного пользователем класса."""
    print("There are some characters on your choice:")
    get_hero_types_info()
    hero_type = int(input("Choose your character (1 - Magician, 2 - Priest, 0 - get random): "))
    if hero_type == 1:
        return create_new_magician()
    elif hero_type == 2:
        return create_new_priest()
    else:
        return create_new_random_hero()


def create_new_random_hero():
    """Метод создания нового персонажа случайного класса."""
    random_choice = randint(1, 2)
    if random_choice == 1:
        return create_new_magician()
    else:
        return create_new_priest()




