from vote.domain.service.voting import VotingService


class VotingApi:

    def voting(self):
        voting_svc = VotingService()
        voting_svc.voting(user_id=1, player_id=4)


if __name__ == '__main__':
    VotingApi().voting()
