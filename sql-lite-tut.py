import sqlite3
# store data in memory, deletes when program exits
# conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('weights.db')
# Create a curor
c = conn.cursor()

# # // create a table
c.execute(("CREATE TABLE weights(date TEXT, weight INT)"))

# # // Insert
# c.execute("INSERT INTO customers VALUES ('Mary', 'Jones', 'mj@gmail.com' )")

# # //Insert many
# many_customers = [('Wes', 'Brown', 'wb@gmail,com'),
#                  ('Steven', 'George', 'steve@mail.com'),
#                  ('Angela', 'Brim', 'ab@gmail.com')
#                  ]
# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# // Query the DB
c.execute("SELECT * FROM customers")
# c.fetchone()
#c.fetchmany(3)
# items = c.fetchone()

#weights c.execute("SELECT * FROM customers WHERE last_n = 'Spikes'")
# c.execute("SELECT * FROM customers WHERE last_n LIKE 'Br%'")

# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
# items = c.fetchall()
# print(items)
# # # #

# commit our command
conn.commit()
# close connection
conn.close
