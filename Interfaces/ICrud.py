from abc import abstractmethod
from abc import ABCMeta

class ICrud(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        raise Exception("Error al llamar método Abstracto.")

    @abstractmethod
    def read(self):
        raise Exception("Error al llamar método Abstracto.")

    @abstractmethod
    def relation(self):
        raise Exception("Error al llamar método Abstracto.")