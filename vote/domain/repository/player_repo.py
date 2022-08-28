from vote.domain.repository.base import Repository

players = [
    dict(id=4, name="robin", day_votes=1),
    dict(id=5, name="enos", day_votes=4),
    dict(id=6, name="anda", day_votes=6),
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
            if player['id'] == id:
                self.current_player = player
                return player
        return None

    def get_day_votes(self):
        return self.current_player.get('day_votes')

    def add_day_votes(self, id):
        print(f"player id={id} day_votes add 1")
        # todo save to db
        self.current_player['day_votes'] += 1
