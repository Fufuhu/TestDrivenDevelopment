
class Doller():

    def __init__(self, amount):
        self.amount = amount
    
    def times(self, multiplier):
        return Doller(self.amount * multiplier)


    def _get_amount(self):
        return self.__amount
    
    def _set_amount(self, amount):
        self.__amount = amount

    amount = property(_get_amount, _set_amount)