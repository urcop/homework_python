import psycopg2
from psycopg2.extras import RealDictCursor

from config import *


class Database:
    def __init__(self):
        self.connect = psycopg2.connect(database=DB_NAME, user=DB_USER,
                                        password=DB_PASSWORD, host=DB_HOST, port=DB_PORT,
                                        cursor_factory=RealDictCursor)
        self.cursor = self.connect.cursor()
        self.execute = self.cursor.execute

    def create_table_users(self):
        self.execute("""
            create table if not exists users(
                first_name varchar(255) not null,
                last_name varchar(255) not null,
                age int not null
            );
        """)
        self.connect.commit()

    def create_table_cats(self):
        self.execute("""
            create table if not exists cats(
                first_name varchar(255) not null,
                last_name varchar(255) not null,
                age int not null
            );
        """)
        self.connect.commit()

    def select(self, table, condition):
        self.execute("""
            select * from {0} where {1};
        """.format(table, condition))
        self.connect.commit()
        return self.cursor.fetchall()

    def insert(self, table, f_n, l_n, age):
        self.execute("""
            insert into {0} (first_name, last_name, age) values (%s, %s, %s)
        """.format(table), (f_n, l_n, age))
        self.connect.commit()
