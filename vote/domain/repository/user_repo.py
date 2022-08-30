from vote.domain.repository.base import Repository
from vote.domain.utils import get_users_db


class UserRepository(Repository):

    def add(self, obj):
        ...

    def remove(self, id):
        ...

    def update(self, id, obj):
        ...

    def get(self, id):
        users = get_users_db()
        for user in users:
            if user.id == id:
                return user
        return None
