from vote.domain.base.entity import Entity


class AggregateRoot(Entity):
    def __init__(self, id):
        Entity.__init__(self, id)
