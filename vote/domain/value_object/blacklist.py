from typing import List

from vote.domain.base.vo import ValueObject
from vote.domain.entity.voter import Voter
from vote.domain.repository import check_repo


class VoteCheck(ValueObject):
    """VoteCheck ValueObject"""

    @property
    def blacklist(self) -> List[str]:
        return check_repo.get_black_list()

    def check(self, voter: Voter):
        """各项检查"""
        # 黑名单检查
        self.check_blacklist(voter.uname)
        # 其他检查

    @classmethod
    def check_blacklist(cls, uname: str) -> bool:
        return uname in check_repo.get_black_list()
