from tests.base import BaseTestSetup

from app.entities.pair import Pair
from app.repositories.pair_repository import PairRepository

class TestPairRepository(BaseTestSetup):

    def test_create(self):
        pair_repo = PairRepository(self.session)
        pair = Pair('GBP/JPY')
        saved_pair = pair_repo.create(pair)

        count = self.session.query(Pair).count()

        self.assertEqual(count, 1)

