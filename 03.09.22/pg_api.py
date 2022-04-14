import psycopg2


def connect_db():
    conn = psycopg2.connect(dbname='python', user='postgres',
                            password='localconnect', host='localhost')
    return conn


def create_table_equipments():
    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Equipments (title varchar(255), count varchar(255), holder Holder );"
    )
    connect.commit()


def create_table_holder():
    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Holder (name varchar(255), phone varchar(255));"
    )
    connect.commit()


def create_table_languages():
    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Languages (
            id serial primary key,
            name varchar(255), 
            quality varchar(255)
        );"""
    )
    connect.commit()


def drop_table_holder():
    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute('DROP TABLE Holder CASCADE;')
    connect.commit()


def drop_table_equipments():
    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute('DROP TABLE Holder CASCADE;')
    connect.commit()


def add_holder(name, phone):
    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute(
        'INSERT INTO Holder (name, phone) VALUES (%s, %s)', (name, phone)
    )
    connect.commit()


def add_language(name, quality):
    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute(
        'INSERT INTO Languages (name, quality) VALUES (%s, %s);', (name, quality)
    )
    connect.commit()


def select_languages():
    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute("select * from languages;")
    connect.commit()
    return cursor.fetchall()


def delete_all_language():
    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute('DELETE FROM languages;')
    connect.commit()
