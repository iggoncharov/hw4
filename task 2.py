import random
from abc import ABC, abstractmethod

class EmojiMixin:
    """
    Mixin класс, который заменяет в классе Pokemon при выводе
    poketype на emogy
    """
    emogy = {'grass': '🌿',
             'fire': '🔥',
             'water': '🌊',
             'electric': '⚡'}

    def __str__(self):
        poketype = super().__str__()
        if self.poketype in self.emogy:
            return poketype.replace(self.poketype, self.emogy[self.poketype])
        else:
            return poketype

class BasePokemon:
    """
    Базовый класс покемона, который выводит name и poketype через '/'
    """
    def __str__(self):
        return f'{self.name}/{self.poketype}'

class AnimeMon(ABC):
    """
    Абстрактный класс анемомонов, который имеет метод 'inc_exp' и свойство 'exp'
    """
    @abstractmethod
    def inc_exp(self, value: int):
        pass

    @property
    @abstractmethod
    def exp(self):
        pass

class Pokemon(EmojiMixin, BasePokemon, AnimeMon):
    """
    Основной класс покемонов, имеет атрибуты: name, poketype
    Свойство "exp" хранит опыт
    Метод inc_exp увеличивает опыт на значение value
    """
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype
        self.__exp = 0

    @property
    def exp(self) -> int:
        return self.__exp

    @exp.setter
    def exp(self, new: int):
        self.__exp = new

    def inc_exp(self, value: int):
        self.exp += value

class Digimon(AnimeMon):
    """
    Класс дигимонов, имеет атрибут: name
    Свойство "exp" хранит опыт
    Метод inc_exp увеличивает опыт на значение value * 8
    """
    def __init__(self, name: str):
        self.name = name
        self.__exp = 0

    @property
    def exp(self) -> int:
        return self.__exp

    @exp.setter
    def exp(self, new: int):
        self.__exp = new

    def inc_exp(self, value: int):
        self.exp += value * 8

def train(pokemon: AnimeMon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - pokemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            pokemon.inc_exp(step_size)

if __name__ == '__main__':

    # Работа класс Pokemon
    print('класс Pokemon:')
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    print(bulbasaur.exp)
    train(bulbasaur)
    print(bulbasaur.exp)
    print()

    # Работа класса Digimon
    print('класс Digimon:')
    dig = Digimon(name = 'Igor')
    print(dig.exp)
    train(dig)
    print(dig.exp)

