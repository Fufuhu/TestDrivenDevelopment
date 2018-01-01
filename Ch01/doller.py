
class Doller():

    def __init__(self, amount):
        self.__amount = amount
    
    def times(self, multiplier):
        self.amount = self.amount * multiplier


    def _get_amount(self):
        return self.__amount
    
    def _set_amount(self, amount):
        self.__amount = amount

    amount = property(_get_amount, _set_amount)