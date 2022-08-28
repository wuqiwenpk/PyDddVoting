from vote.domain.base.aggregate_root import AggregateRoot


class Voter(AggregateRoot):
    """Voter Entity & AggregateRoot"""
    id: int
    user_id: int
    prize_id: int

    def __init__(self, user_id):
        AggregateRoot.__init__(self, user_id)

    def voting(self) -> str:
        """开始投票"""
        pass


v = Voter(user_id=110)
print(v.id)
