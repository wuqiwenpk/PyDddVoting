from vote.domain.base.entity import Entity


class User(Entity):
    """User Entity"""
    id: int
    name: str
    age: int

    def __init__(self, id):
        Entity.__init__(self, id)

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age
