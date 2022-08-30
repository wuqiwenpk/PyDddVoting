from vote.domain.repository.base import Repository
from vote.domain.utils import get_player_db, set_player_db


class PlayerRepository(Repository):
    current_player = None

    def add(self, obj):
        ...

    def remove(self, id):
        ...

    def update(self, id, obj):
        ...

    def get(self, id):
        players = get_player_db()
        for player in players:
            if player.id == id:
                return player
        return None

    def list(self):
        return get_player_db()

    def get_day_votes(self):
        return self.current_player.day_votes

    def add_day_votes(self, id):
        players = self.list()
        for player in players:
            if player.id == id:
                player.day_votes += 1
                print(f"选手{player.name}[{player.id}] 票数 + 1 总票数为: {player.day_votes}")
        print("########### 实时票数 ##############")
        for player in self.list():
            print(f"选手{player.name}[{player.id}] 票数：{player.day_votes}")
        print("##################################")
        set_player_db(players)

    def get_max_day_votes_player_id(self):
        players = self.list()
        players.sort(key=lambda s: s.day_votes, reverse=True)
        return players[0].id
