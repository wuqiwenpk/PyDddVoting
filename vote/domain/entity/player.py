from vote.domain.base.entity import Entity
from vote.domain.repository import player_repo


class Player(Entity):
    """Player Entity"""

    def __init__(self, id):
        Entity.__init__(self, id)
        self._player = player_repo.get(id)

    @property
    def uname(self):
        return self._player.name

    @property
    def day_votes(self) -> int:
        return self._player.day_votes

    def add_day_votes(self):
        player_repo.add_day_votes(self.id)

    def receive(self, goods_name: str):
        """接受奖品"""
        # todo add new Address Entity
        print(f"选手:{self._player.name} 获得了奖品:{goods_name}")
