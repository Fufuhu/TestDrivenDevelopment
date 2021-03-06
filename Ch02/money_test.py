import unittest

from doller import Doller

class MoneyTest(unittest.TestCase):
    
    def test_multiplication(self):
                five = Doller(amount=5)
                product = five.times(2)
                self.assertEqual(10, product.amount)
                product = five.times(3)
                self.assertEqual(15, product.amount)



if __name__ == '__main__':
    unittest.main()