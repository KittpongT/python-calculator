import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 1 + 2)
        self.assertEqual(self.calc.add(-2, -5), -2 + -5)

    def test_substract(self):
        self.assertEqual(self.calc.subtract(2, -5), 2 - -5)
        self.assertEqual(self.calc.subtract(-12, -2), -12 - - 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(0, 2), 0 * 2)
        self.assertEqual(self.calc.multiply(-5, -8), -5 * -8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 5), 2 // 5)
        self.assertEqual(self.calc.divide(-20, 10), -20 // 10)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(8, 3), 8 % 3)
        self.assertEqual(self.calc.modulo(-1, 4), -1 % 4)
    

if __name__ == '__main__':
    unittest.main()
