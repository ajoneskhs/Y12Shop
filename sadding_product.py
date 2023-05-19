#System to estimate realisitc price per product
  #nothing over £10k, float, must not be <0

#Method to add a product
  #Takes in the name and price of the product
  #Gives back primary key


class Product:
  def __init__(self, productID, productType, productPrice, productName):
    self.productID = productID
    self.producType = productType
    self.productName = productName
    self.productPrice = productPrice



  
  def add_product(self, productID, productType, productPrice, productName):
    if self.productPrice >= 10000:
      return False
    elif self.productPrice <0:
      return False
    elif self.productPrice <= 10000:
      return True
    elif self.productName != "offensive word": #need for loop to check each letters/words in the Name to check for appropiate name 
      return True
    
  
  def delete_product():
    
    pass

  