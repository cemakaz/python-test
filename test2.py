import unittest
import warnings

warnings.filterwarnings("ignore")

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def to_uppercase(s):
    return s.upper()

class TestStringFunctions(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("Python"))
        self.assertTrue(is_palindrome(""))

    def test_to_uppercase(self):
        self.assertEqual(to_uppercase("hello"), "HELLO")
        self.assertEqual(to_uppercase("world"), "WORLD")
        self.assertEqual(to_uppercase("Python"), "PYTHON")
        self.assertEqual(to_uppercase(""), "")

if __name__ == '__main__':
    unittest.main()
