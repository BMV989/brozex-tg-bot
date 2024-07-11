from enum import Enum, unique


@unique
class Commands(Enum):


    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description
