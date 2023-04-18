import unittest
from palindromo import palindromo


class TestPalindrome(unittest.TestCase):
    def test_palindromo_simple(self):
        result = palindromo('neuquen')
        self.assertEqual(result, True)
    
    def test_palindromo_2(self):
        result = palindromo("ana")
        self.assertEqual(result,True)
    
    def test_palindromo_(self):
        result = palindromo("oso")
        self.assertSetEqual(result,True)
    


if __name__== '__main__':
    unittest.main()