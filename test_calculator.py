# https://github.com/TyH979/lab11-THH-YRT
# Partner 1: Ty Holmgren
# Partner 2: Yoav Tsadok
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(multiply(4, 8), 32)
        self.assertEqual(multiply(-2, 2), -4)
        self.assertEqual(multiply(0, 1), 0)

    
    def test_divide(self):
        self.assertEqual(divide(5, 10), 2)
        self.assertEqual(divide(-4, 8), -2)
        self.assertEqual(divide(7, 0), 0.0) 
    ###########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
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
