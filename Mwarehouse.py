class Warehouse:
	def __init__(self, warehouseadd):
		W_location = warehouseadd
	def recieve(self,goodsID,checksum):
    	for i in range(0,len(goodsID)):
            cs = generateChecksum(goodsID[i])
            if cs != checksum[i]:
                print("item",goodsID[i],"has been declined")
	def dispatch(self, goodsID, address, delivery_standard):
		pass
	def get_num(self, name:str):
		#get name of item, return quantity from database
        return(quantity)
	def delivery_estimate(self, postcode:str):
		AddressFinder.poscode2list(postcode)