import mysql.connector
import functools
import pandas

cars = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="classicmodels",
    port="3306"
)

stateQun = cars.cursor()
stateQun.execute("SELECT state FROM customers GROUP BY state,city")
stateresult = stateQun.fetchall()
state = []

for i in stateresult:
    res = functools.reduce(lambda sub, ele: sub * 10 + ele, i)
    i = str(res)
    state.append(str(res))

cityQun = cars.cursor()
cityQun.execute("SELECT city FROM customers GROUP BY city, state")
cityresult = cityQun.fetchall()
cities = []

for i in cityresult:
    res = functools.reduce(lambda sub, ele: sub * 10 + ele, i)
    i = str(res)
    cities.append(str(res))

countQun = cars.cursor()
countQun.execute("SELECT COUNT(city) FROM customers GROUP BY city, state")
countresult = countQun.fetchall()
count = []

for i in countresult:
    res = functools.reduce(lambda sub, ele: sub * 10 + ele, i)
    i = str(res)
    count.append(int(res))

average = []

totalOrders = 0
for x in count:
    totalOrders = totalOrders + x

for i in count:
    average.append(f"{i / totalOrders:.0%}")

order_data = {
    "State": state,
    "City": cities,
    "Count": count,
    "Average": average
}

print(len(state))
print(len(cities))


publish_data = pandas.DataFrame(order_data)
#print(publish_data)
publish_data.to_csv("publish_data.csv")
