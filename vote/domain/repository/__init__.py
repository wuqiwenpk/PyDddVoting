"""Repository"""
from vote.domain.repository.player_repo import PlayerRepository
from vote.domain.repository.user_repo import UserRepository
from vote.domain.repository.check_repo import CheckRepository
from vote.domain.repository.goods_repo import GoodsRepository

user_repo = UserRepository()
player_repo = PlayerRepository()
check_repo = CheckRepository()
goods_repo = GoodsRepository()
