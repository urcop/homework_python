import psycopg2
from psycopg2.extras import RealDictCursor


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(database="main_db", user='urcop',
                                     password='localconnect', host='localhost', port=5432,
                                     cursor_factory=RealDictCursor)

    def select_tour(self):
        cursor = self.conn.cursor()
        cursor.execute("select * from tour;")
        self.conn.commit()
        return cursor.fetchall()

    def select_review(self):
        cursor = self.conn.cursor()
        cursor.execute("select * from review;")
        self.conn.commit()
        return cursor.fetchall()
