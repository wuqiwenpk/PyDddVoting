"""Repository"""
from vote.domain.repository.player_repo import PlayerRepository
from vote.domain.repository.user_repo import UserRepository

user_repo = UserRepository()
player_repo = PlayerRepository()
