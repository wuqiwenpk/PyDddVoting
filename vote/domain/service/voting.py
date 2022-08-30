"""Voting domain service"""
from vote.domain.entity.player import Player
from vote.domain.entity.voter import Voter
from vote.domain.value_object.blacklist import VoteCheck


class VotingService:
    """Voting service"""

    @classmethod
    def voting(cls, user_id: int, player_id: int):
        """开始投票"""

        # 获取投票者
        voter = Voter(user_id)
        # 风控检查
        vote_check = VoteCheck()
        vote_check.check(voter)
        # 获取选手
        player = Player(player_id)
        # 投票,选手票数+1
        voter.voting(player)

        return dict(success=True, msg="投票成功")

    @classmethod
    def get_player_day_votes(cls, player_id: int):
        """获取选手票数"""
        player = Player(player_id)
        return player.day_votes
