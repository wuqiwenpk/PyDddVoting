from vote.domain.repository.base import Repository


class Player_:
    def __init__(self, id, name, day_votes):
        self.id: int = id
        self.name: str = name
        self.day_votes: int = day_votes


players = [
    Player_(id=4, name="robin", day_votes=1),
    Player_(id=5, name="enos", day_votes=4),
    Player_(id=6, name="anda", day_votes=6),
]


class PlayerRepository(Repository):
    current_player = None

    def add(self, obj):
        ...

    def remove(self, id):
        ...

    def update(self, id, obj):
        ...

    def get(self, id):
        # todo get by orm
        for player in players:
            if player.id == id:
                self.current_player = player
                return player
        return None

    def get_day_votes(self):
        return self.current_player.day_votes

    def add_day_votes(self, id):

        self.current_player.day_votes += 1
        print(f"player id={id} day_votes + 1 total: {self.current_player.day_votes}")
        # todo save to db

    def get_max_day_votes_player_id(self):
        return 6
