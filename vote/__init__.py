from flask import Flask
from flask_restful import Api

from vote.interfaces.voting import VotingApi


def create_app():
    app = Flask(__name__)
    reg_api(app)
    init_mock_data()

    return app


def reg_api(app):
    api = Api(app)
    api.add_resource(VotingApi, "/voting")


def init_mock_data():
    from vote.domain.utils import set_users_db, set_player_db

    class User:
        def __init__(self, id, name, age):
            self.id: int = id
            self.name: str = name
            self.age: int = age
    users = [
        User(id=1, name="tom", age=11),
        User(id=2, name="jack", age=42),
        User(id=3, name="rose", age=26),
    ]

    class Player:
        def __init__(self, id, name, day_votes):
            self.id: int = id
            self.name: str = name
            self.day_votes: int = day_votes

    players = [
        Player(id=4, name="robin", day_votes=3),
        Player(id=5, name="enos", day_votes=1),
        Player(id=6, name="anda", day_votes=2),
    ]
    set_users_db(users)
    set_player_db(players)
