#//Check Details\\#
# The check details function validates the payment information provided. it needs a payment type e.g. 'card'
# The check details function also needs a list with the details such as cardnumber, CCV, expiry date, etc.

#//Charge\\#
# The charge function needs a price, stored in the custom variable of currency including the price and the currency
# The payment details are also needed once again to make the payment

#//Confirmation\\#
# The conformation function interprets the response from the payment provider, confirming if the payment failed or went through
# It will return the output from the payment provider, allowing an appropriate error to be displayed to the user.

class Payment:
    def __init__(self):
        pass

    def checkDetails(self, paymentType: str, paymentDetails: list[str, int, float]):
        pass

    def charge(self, price: Currency, paymentDetails: list[str, int, float]):
        pass

    def confirmation(self):
        pass
 