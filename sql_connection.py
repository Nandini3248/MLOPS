# sql_connection.py

class SQLConnection:
    def __init__(self):
        self.connection_status = "Connected to In-Memory CRUD Engine"

    def get_status(self):
        return self.connection_status


def get_db_connection():
    return SQLConnection()