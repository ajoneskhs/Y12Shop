from Zdb import dbConnector

class AddressFinder:
    def __init__(self):
        x = dbConnector()
        self.connector = x.connect()

    def postcodeFinder(self, postcode: str):
        self.connector.execute("SELECT * FROM postcodes WHERE postcode = '"+postcode+"'")
        data = self.connector.fetchall()
        for line in data:
            print(line)

#x = AddressFinder()
#x.postcode2town("TW8")




        
    



