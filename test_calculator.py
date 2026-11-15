# https://github.com/TyH979/lab11-THH-YRT
# Partner 1: Ty Holmgren
# Partner 2: Yoav Tsadok
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(4, 8), 12)
        self.assertEqual(add(-2, 2), 0)
        self.assertEqual(add(0, 1), 1)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(40, 8), 32)
        self.assertEqual(subtract(-2, 2), -4)
        self.assertEqual(subtract(0, 1), -1)
    ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(4, 8), 32)
        self.assertEqual(mul(-2, 2), -4)
        self.assertEqual(mul(0, 1), 0)

    
    def test_divide(self):
        self.assertEqual(div(5, 10), 2)
        self.assertEqual(div(-4, 8), -2)
        self.assertEqual(div(7, 0), 0.0) 
    ###########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
         with self.assertRaises(ValueError):
             div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(16, 64), 1.5)
        self.assertEqual(logarithm(7, 1), 0) 

    def test_log_invalid_base(self): # 1 assertion
         with self.assertRaises(ValueError):
             logarithm(0, 5)
    ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)

    def test_sqrt(self): # 3 assertions
        #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(16), 4)  
        ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
