import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS weight_records (id INTEGER PRIMARY KEY, date text, weight int)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * from weight_records")
        rows = self.cur.fetchall()
        return rows

    def insert(self, date, weight):
        self.cur.execute("INSERT INTO weight_records VALUES (NULL, ?, ?)", (date, weight))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM weight_records WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, date, weight):
        self.cur.execute("UPDATE weight_records SET date = ?, weight = ? WHERE id = ?",
                         (date, weight, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# db = Database('weight_app.db')
# db.insert("19/11/2021", 171)
# db.insert("20/11/2021", 161)
# db.insert("12/11/2021", 175)
# db.insert("13/11/2021", 131)
# db.insert("11/11/2021", 111)
