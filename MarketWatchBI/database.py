import sqlite3
from sqlite3 import Error


class Database(object):

    def __init__(self, name):
        try:
            self.conn = sqlite3.connect(name)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()

    # Returns data
    def select(self, table_name):
        return ''

    # Insert data, returns 1 for success
    def insert(self, table_name, data, time):
        return ''
