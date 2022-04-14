import pprint
from pprint import pprint

from db_api import Database

db = Database()

db.create_table_users()
db.create_table_cats()
db.insert('cats', 'oleg', 'jopa', 15)
db.insert('cats', 'oleg', 'ss', 15)
db.insert('cats', 'oleg', 'sss', 15)
db.insert('cats', 'oleg', 'sssss', 15)

db.insert('users', 'nikolai', 'ssss', 200)
db.insert('users', 'nikolai', 's', 200)
db.insert('users', 'nikolai', 'sw', 200)
db.insert('users', 'nikolai', 'ss', 200)
db.insert('users', 'nikolai', 'sss', 200)


cats = db.select('cats', "first_name='oleg'")
users = db.select('users', "first_name='nikolai'")
for cat in cats:
    pprint(dict(cat))


