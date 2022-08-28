class Entity:

    def __init__(self, id):
        self._id = id

    def __eq__(self, other):
        return self._id == other.id

    @property
    def id(self):
        return self._id
