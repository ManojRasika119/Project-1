import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table =  "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'Manoj', '1234')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

print (user)

user = (2, 'Ashan', '4645')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

print (user)

user = (3, 'Danangi', '9809')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

print (user)

user = (4, 'Prathibha', '5731')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

print (user)

user = (5, 'Jane', '86543')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

print (user)

connection.commit()
connection.close()
