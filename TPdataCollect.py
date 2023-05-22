from Zdb import dbConnector
class DataCollector:
  def __init__(self):
    x = dbConnector()
    self.connector = x.connect()

  def recordEvent(self,originModule, ip, instruction, isMajor):
    if isMajor:
      isMajor = 1
    else:
      isMajor = 0
    query = "INSERT INTO log (originModule, IP, instruction, isMajor) VALUES (%s, %s, %s, %s)"
    self.connector.execute(query, (originModule,ip,instruction,isMajor,))
    self.connector.commit()

    pass

#  def accounts(self, ):
#    pass
#def loginActivity(self, ):
#    pass
#def productsDifference(self, ):
#   pass
