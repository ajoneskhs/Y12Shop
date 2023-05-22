#//Common Themes\\#
# The getCommonThemes function uses the list of the users previously purchased and uses the catagories of those products to recommend products
# An extension to this code would allow it to display currently trending items to be recommended to new users

#//Simlair Products\\#
# The getSimilairProducts function retrieves products from the database with the same or similair catagories to the users previosuly purchased.
# The function will not recommend products a user has already purchased before, this relies on it being in their previosuly purchased list.

class Recommend:
    def __init__(self):
        pass

    def getCommonThemes(self, PreviouslyPurchased: list[str]):
        pass

    def getSimilairProducts(self, SimilairProducts: list[str], PreviouslyPurchased: list[str]):
        pass
