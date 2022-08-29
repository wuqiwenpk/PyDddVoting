from vote.domain.repository.base import Repository


class User:
    def __init__(self, id, name, age):
        self.id: int = id
        self.name: str = name
        self.age: int = age


users = [
    User(id=1, name="tom", age=11),
    User(id=2, name="jack", age=42),
    User(id=3, name="rose", age=26),
]


class UserRepository(Repository):

    def add(self, obj):
        ...

    def remove(self, id):
        ...

    def update(self, id, obj):
        ...

    def get(self, id):
        for user in users:
            if user.id == id:
                return user
        return None
