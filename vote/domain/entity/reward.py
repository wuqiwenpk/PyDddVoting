from vote.domain.base.aggregate_root import AggregateRoot
from vote.domain.base.entity import Entity
from vote.domain.entity.player import Player
from vote.domain.repository import user_repo, goods_repo


class Reward(Entity):
    """Reward Entity & AggregateRoot"""

    def __init__(self, goods_id):
        Entity.__init__(self, goods_id)

    def check_goods_enough(self):
        """检查商品是否还有"""
        return True if goods_repo.get(self.id).count else False

    def award_prizes(self):
        """发奖"""
        goods_repo.award_prizes(self.id)
