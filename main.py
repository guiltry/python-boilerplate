from app.config.database import Database

if __name__ == '__main__':
    database = Database()
    database.migrate()
