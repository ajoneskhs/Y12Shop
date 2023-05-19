import pymysql

class dbConnector():
    def __init__(self):
        pass
    def connect(self):
        db = pymysql.connect(host= "77.68.35.85",user="y12shop", password="Ni64e2u_9", database= "y12shop")

        cursor = db.cursor()
        return cursor

    

