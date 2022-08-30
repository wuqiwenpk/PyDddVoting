import os.path

from pathlib import Path

import dill


class User:
    def __init__(self, id, name, age):
        self.id: int = id
        self.name: str = name
        self.age: int = age


def get_users_db() -> list:
    pkl_file = open(os.path.join(str(Path(__file__).parent.parent), "db/users.db"), 'rb')
    res = dill.load(pkl_file)
    pkl_file.close()
    return res


def set_users_db(users):
    pkl_file = open(os.path.join(str(Path(__file__).parent.parent), "db/users.db"), 'wb')
    dill.dump(users, pkl_file)
    pkl_file.close()


def get_player_db() -> list:
    pkl_file = open(os.path.join(str(Path(__file__).parent.parent), "db/players.db"), 'rb')
    res = dill.load(pkl_file)
    pkl_file.close()
    return res


def set_player_db(players):
    pkl_file = open(os.path.join(str(Path(__file__).parent.parent), "db/players.db"), 'wb')
    dill.dump(players, pkl_file)
    pkl_file.close()
