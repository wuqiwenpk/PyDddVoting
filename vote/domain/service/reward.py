"""Reward domain service"""
from vote.domain.entity.reward import Reward
from vote.domain.entity.player import Player
from vote.domain.repository import goods_repo, player_repo


class RewardService:
    """Reward service"""

    @classmethod
    def reward(cls, player_id: int):
        """发奖"""
        # 获取选手
        player = Player(player_id)
        # 从商品库中随机挑一件商品
        goods = goods_repo.goods_choice()
        # 发奖前库存判断
        reward = Reward(goods.id)
        if not reward.check_goods_enough():
            print("很遗憾 该商品库存不足，终止发奖 😼")
            return None
        # 发奖 库存减1
        reward.award_prizes()
        # 选手接收奖品
        player.receive(goods.name)

    @classmethod
    def get_max_day_votes_player_id(cls):
        """获取当前票数最多选手id"""
        return player_repo.get_max_day_votes_player_id()


if __name__ == '__main__':
    a = RewardService()
    a.reward(4)
