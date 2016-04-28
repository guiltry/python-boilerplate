from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Database(object):
    def __init__(self, env = 'development'):
        self._generate_engine(env)

    def _generate_engine(self, env):
        self.engine = create_engine('postgresql://username@host/app_' + env, echo=False)

    def get_session(self):
        return sessionmaker(bind=self.engine)

    def migrate(self):
        Base.metadata.create_all(self.engine)

    def drop(self):
        Base.metadata.drop_all(self.engine)

