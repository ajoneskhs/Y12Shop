import pymysql
db = pymysql.connect("77.68.35.85")

mycursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print(data)

db.close()
