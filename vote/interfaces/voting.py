from flask import request
from vote.domain.service.voting import VotingService

from flask_restful import Resource


class VotingApi(Resource):
    def post(self):

        user_id = request.json.get("user_id")
        player_id = request.json.get("player_id")
        voting_svc = VotingService()
        return voting_svc.voting(user_id=user_id, player_id=player_id)
