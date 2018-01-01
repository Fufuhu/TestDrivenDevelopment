import unittest

from doller import Doller

class MoneyTest(unittest.TestCase):
    
    def test_multiplication(self):
                five = Doller(amount=5)
                five.times(2)
                self.assertEqual(10, five.amount)



if __name__ == '__main__':
    unittest.main()