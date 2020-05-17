import sqlite3

connection = sqlite3.connect('data.db') # to connect to "data.db" data base
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# to create non exising new users with id username and password
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
# to create non exising new items
cursor.execute("INSERT INTO items VALUES ('test', 10.99)")

connection.commit()

connection.close()
