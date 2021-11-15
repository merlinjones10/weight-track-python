import sqlite3

conn = sqlite3.connect('weights.db')

try:
    conn = sqlite3.connect('weights.db')
    print("Connection successful")
except:
    print('Failed to connect')

c = conn.cursor()

#records or rows in a list
weightRecords = [
                ('15/11/2021', 79),
                ('15/11/2021', 79),
                ('15/11/2021', 79),
                ('15/11/2021', 79),
                ('15/11/2021', 79),
                ('15/11/2021', 79),
                ('15/11/2021', 79),
                ]

#insert multiple records in a single query
c.executemany('INSERT INTO weights VALUES(?,?);',weightRecords);

print('We have inserted', c.rowcount, 'records to the table.')

#commit the changes to db
conn.commit()
#close the connection
conn.close()