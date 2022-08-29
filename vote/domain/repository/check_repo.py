from vote.domain.repository.base import Repository

BLACKLIST = ["tom", "tom1", "tom2"]


class CheckRepository(Repository):

    def add(self, obj):
        ...

    def remove(self, id):
        ...

    def update(self, id, obj):
        ...

    def get(self, id):
        ...

    @classmethod
    def get_black_list(cls):
        return BLACKLIST
