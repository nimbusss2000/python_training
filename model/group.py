
from sys import maxsize

class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        # сравнение двух тестов с упорядоченными значениями id-имя

        return f'{self.id}, {self.name}, {self.header}, {self.footer}'

    def __eq__(self, other):
        # т.к питон учитывает еще и место в памяти каждого id (оно у всех разное), то нужно сделать сравнениe логическим,
        # а не физическим

        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


