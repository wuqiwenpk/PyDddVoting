from vote.domain.base.entity import Entity
from vote.domain.repository import player_repo


class Player(Entity):
    """Player Entity"""

    def __init__(self, id):
        Entity.__init__(self, id)

    @property
    def day_votes(self) -> int:
        return player_repo.get_day_votes()

    def add_day_votes(self):
        player_repo.add_day_votes(self.id)


if __name__ == '__main__':
    player_repo.get(4)
    p1 = Player(id=4)
    print(p1.day_votes)
    p1.add_day_votes()
    print(p1.day_votes)
