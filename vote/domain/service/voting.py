"""Voting domain service"""
from vote.domain.repository import user_repo, player_repo


class VotingService(object):

    def voting(self, user_id, player_id):
        """do voting"""
        # get voter message
        user = user_repo.get(user_id)
        player = player_repo.get(player_id)
        print(f"user {user}")
        print(f"player {player}")


if __name__ == '__main__':
    v = VotingService()
    v.voting(user_id=1, player_id=4)
