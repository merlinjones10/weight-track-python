from datetime import date
import sqlite3
# 79kg
# GLOBAL VARIABLES
conn = sqlite3.connect('weights.db')
c = conn.cursor()
today = date.today().strftime("%d/%m/%Y")
dayInWeek = date.today().strftime("%a")

print(today)
#  CLASSES
class Measurement:
    def __init__(self, weight):
        self.weight = weight
        self.date = today


# FUNCTIONS
def calcAvg(weights):
    return round(sum(weights) / 7, 1)


def kgToLbs(kgs):
    pounds = kgs * 2.2046
    return pounds


def takeMeasurement():
    todaysMeasurement = int(input("Enter today's weight: "))
    currentWeight = Measurement(todaysMeasurement)
    c.execute("INSERT INTO weights VALUES (?, ?)", (currentWeight.date, currentWeight.weight))
    conn.commit()
    print('Entry successful')


def displayAverage():
    if input('Show weeks weights and average? (y/n): ').lower() == 'n':
        print('See you tomorrow')
    else:
        displayEach()


def displayEach():
    c.execute("SELECT * FROM weights")
    items = c.fetchall()
    allWeights = [x[1] for x in items]
    averageWeight = calcAvg(allWeights)
    lbsConversion = round(kgToLbs(averageWeight), 2)
    print('Weeks weights: ')
    for item in items:
        print(f"-{item[0]}  \t - {item[1]}kg")
    print(f"\nAverage: {averageWeight}kg --- or --- {lbsConversion}lbs ")


# ------------ PROGRAM FLOW --------------- #
takeMeasurement()
# displayAverage()
conn.close()

#  ------------- fragments ------------ #
# c.execute("INSERT INTO weights VALUES ('date', 23)")
# take_measurement()
# displayEach()
# sample_week_weights = [12, 13, 12, 14, 14, 12, 11]
#
# if 'Fri' == 'Fri':
#     avg = calcAvg(sample_week_weights)
#     print(f"Average weight is {avg}")
# c.execute(("CREATE TABLE weights(date TEXT, weight INT)"))
# c.execute("insert into contacts values(?,?,?)",(name, phone, email))
