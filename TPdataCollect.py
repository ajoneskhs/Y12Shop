from Zdb import dbConnector
class DataCollector:
  def __init__(self):
    x = dbConnector()
    self.connector = x.connect()

  def recordEvent(self,originModule, ip, instruction, isMajor):
    query = "INSERT INTO log (originModule, IP, instruction, isMajor) VALUES (%s, %s, %s, %i)"
    self.connector.execute(query, (originModule,ip,instruction,isMajor))

    pass

#  def accounts(self, ):
#    pass
#def loginActivity(self, ):
#    pass
#def productsDifference(self, ):
#   pass
