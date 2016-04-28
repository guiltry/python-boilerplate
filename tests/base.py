import unittest

from app.config.database import Database

class BaseTestSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.database = Database('testing')
        cls.database.migrate()

        cls.Session = cls.database.get_session()
        cls.session = cls.Session()

    def setUp(self):
        self.session = self.session
        self.session.begin_nested()

    def tearDown(self):
        self.session.rollback()
