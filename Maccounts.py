# user first and last names
#user age/gender
#user addresses/ previous purchases

class Account:
	def __init__(self):
		pass
	def name(self,f:str,s:str):
    	self.f_name = f
    	self.s_name = s
	def age (self, year:int):
		pass
	def gender (self, gend:str):
		pass
	def address(self, postcode:str):
		AddressFinder.poscode2list(postcode)

