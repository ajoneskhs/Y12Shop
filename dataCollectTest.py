from TPdataCollect import DataCollector

class TPtest():
  def __init__(self):
    collector = DataCollector()
    collector.recordEvent("LOGIN","34.45.23.12","HACKING ALERT BY USER " ,True)
    

tom = TPtest()