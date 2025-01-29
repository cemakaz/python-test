import unittest
import warnings

warnings.filterwarnings("ignore")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestMathFunctions(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 2), 1)

    def test_add_zeros(self):
        self.assertEqual(add(0, 0), 0)

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-5, -3), -2)

    def test_subtract_mixed_numbers(self):
        self.assertEqual(subtract(5, -3), 8)

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), 6)

    def test_multiply_mixed_numbers(self):
        self.assertEqual(multiply(2, -3), -6)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(2, 0), 0)

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(6, 2), 3)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-6, -2), 3)

    def test_divide_mixed_numbers(self):
        self.assertEqual(divide(6, -2), -3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(6, 0)

if __name__ == '__main__':
    unittest.main()
