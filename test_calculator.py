import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

     # Add a+b
    def test_add_right(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_wrong(self):
        self.assertNotEqual(self.calc.add(1, 2), 8)

    def test_add_onenegative(self):
        self.assertEqual(self.calc.add(1, -2), -1)

    def test_add_bothnegative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    # Subtract a-b
    def test_subtract_right(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_subtract_wrong(self):
        self.assertNotEqual(self.calc.subtract(4, 2), 8)

    def test_subtract_lesssubmore(self):
        self.assertEqual(self.calc.subtract(2, 5), -3)
    
    def test_subtract_firstnegative(self):   
        self.assertEqual(self.calc.subtract(-2, 4), -6)

    def test_subtract_secondnegative(self):
        self.assertEqual(self.calc.subtract(3, -1), 4)

    def test_subtract_bothnegative(self):
        self.assertEqual(self.calc.subtract(-3, -1), -2)

    # Multiply a*b
    def test_multiply_right(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
    
    def test_multiply_wrong(self):
        self.assertNotEqual(self.calc.multiply(2, 3), 8)

    def test_multiply_byzero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_multiply_bothnegative(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiply_onenegative(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    # Divide a/b
    def test_divide_right(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    
    def test_divide_wrong(self):
        self.assertNotEqual(self.calc.divide(10, 2), 8)
    
    def test_divide_indivisible(self):
        self.assertEqual(self.calc.divide(7, 2), 3)

    def test_divide_byone(self):
        self.assertEqual(self.calc.divide(5, 1), 5)
    
    def test_divide_bothnegative(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_onenegative(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
    
    def test_divide_byzero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    # Modulo  a%b
    def test_modulo_right(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_wrong(self):
        self.assertNotEqual(self.calc.modulo(10, 3), 2)

    def test_modulo_a_less_b(self):
        self.assertEqual(self.calc.modulo(2, 5), 2)
    
    def test_modulo_bothnegative(self):
        self.assertEqual(self.calc.modulo(-10, -3), -1)

    def test_modulo_onenegative(self):
        self.assertEqual(self.calc.modulo(-10, 3), -1)
        
    def test_modulo_othernegative(self):
        self.assertEqual(self.calc.modulo(10, -3), 1)

    def test_modulo_byzero(self):
        with self.assertRaises(ValueError):
            self.calc.modulo(5, 0)

if __name__ == '__main__':
    unittest.main()