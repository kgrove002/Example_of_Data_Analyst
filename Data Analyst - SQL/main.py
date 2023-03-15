import mysql.connector
import functools

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="dark_magician",
    port="3308"
)

totalMonstersQun = db.cursor()
totalMonstersQun.execute("SELECT quantity FROM `deck` WHERE type = 'Monster'")
totalMonsterQun = []
for i in totalMonstersQun:
    res = functools.reduce(lambda sub, ele: sub * 10 + ele, i)
    i = str(res)
    totalMonsterQun.append(int(res))
totalMonstersAmount = sum(totalMonsterQun)

atk = db.cursor()
atk.execute("SELECT atk FROM `deck` WHERE atk >= 0")
atkData = []
for i in atk:
    res = functools.reduce(lambda sub, ele: sub * 10 + ele, i)
    i = str(res)
    atkData.append(int(res))

atkQun = db.cursor()
atkQun.execute("SELECT quantity FROM `deck` WHERE atk >= 0")
atkQunData = []
finalAtkData = []
for i in atkQun:
    res = functools.reduce(lambda sub, ele: sub * 10 + ele, i)
    i = str(res)
    atkQunData.append(int(res))
for i in range(len(atkData)):
    finalAtkData.append(atkData[i] * atkQunData[i])
averageAtk = int(sum(finalAtkData) / totalMonstersAmount)
print(f"The total attack of the deck is {sum(finalAtkData)}")
print(f"The average attack of the deck is {averageAtk}")

defe = db.cursor()
defe.execute("SELECT def FROM `deck` WHERE def >= 0")
defData = []
for i in defe:
    res = functools.reduce(lambda sub, ele: sub * 10 + ele, i)
    i = str(res)
    defData.append(int(res))

defQun = db.cursor()
defQun.execute("SELECT quantity FROM `deck` WHERE def >= 0")
defQunData = []
finalDefData = []
for i in defQun:
    res = functools.reduce(lambda sub, ele: sub * 10 + ele, i)
    i = str(res)
    defQunData.append(int(res))
for i in range(len(defData)):
    finalDefData.append(defData[i] * defQunData[i])
averageDef = int(sum(finalDefData) / totalMonstersAmount)
print(f"The total defense of the deck is {sum(finalDefData)}")
print(f"The average defense of the deck is {averageDef}")

level = db.cursor()
level.execute("SELECT level_rank FROM `deck` WHERE level_rank >= 1")
levelData = []
for i in level:
    res = functools.reduce(lambda sub, ele: sub * 10 + ele, i)
    i = str(res)
    levelData.append(int(res))
averageLevel = int(sum(levelData) / totalMonstersAmount)
print(f"The total level of the deck is {sum(levelData)}")
print(f"The average level of the deck is {averageLevel}")
print(f"There are a total of {totalMonstersAmount} monster cards in this deck")
