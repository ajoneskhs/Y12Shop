from Zdb import dbConnector
class DataCollector:
  def __init__(self):
    self.connector = dbConnector()
    pass
  def recordEvent(self,orginModule, ip, instruction, isMajor):
    self.connector.execute("INSERT INTO log (originModule, IP, instruction, isMajor) VALUES ()")

    pass

#  def accounts(self, ):
#    pass
#def loginActivity(self, ):
#    pass
#def productsDifference(self, ):
#   pass
