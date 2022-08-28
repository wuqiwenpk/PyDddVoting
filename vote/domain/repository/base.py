from abc import ABCMeta, abstractmethod


class Repository(metaclass=ABCMeta):

    @abstractmethod
    def add(self, obj):
        ...

    @abstractmethod
    def remove(self, id):
        ...

    @abstractmethod
    def update(self, id, obj):
        ...

    @abstractmethod
    def get(self, id):
        ...
