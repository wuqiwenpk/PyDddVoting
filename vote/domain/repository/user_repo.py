from vote.domain.repository.base import Repository

users = [
    dict(id=1, name="tom", age=11),
    dict(id=2, name="jack", age=42),
    dict(id=3, name="rose", age=26),
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
            if user['id'] == id:
                return user
        return None
