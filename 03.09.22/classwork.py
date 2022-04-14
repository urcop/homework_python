import pg_api as db

db.create_table_languages()
name, quality = map(str, input().split())

db.add_language(name=name, quality=quality)
