from app.config.database import Database
from app.entities.pair import Pair
from app.repositories.pair_repository import PairRepository

if __name__ == '__main__':
    database = Database()
    database.migrate()

    p = Pair('GBP/JPY')
    pair_repo = PairRepository(database.get_session())

    p = pair_repo.create(p)
    print(p.id)

