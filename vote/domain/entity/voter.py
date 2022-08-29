from vote.domain.base.aggregate_root import AggregateRoot
from vote.domain.entity.player import Player
from vote.domain.repository import user_repo


class Voter(AggregateRoot):
    """Voter Entity & AggregateRoot"""

    def __init__(self, user_id):
        AggregateRoot.__init__(self, user_id)
        self._user = user_repo.get(user_id)

    @property
    def uname(self):
        return self._user.name

    @classmethod
    def voting(cls, player: Player):
        """开始投票"""
        # 选手增加票数
        player.add_day_votes()
