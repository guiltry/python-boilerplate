from app.entities.pair import Pair

class PairRepository(object):
    def __init__(self, session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        self.session.commit()

        return entity
