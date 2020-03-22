import unittest
from main import add

class MyTestCase(unittest.TestCase):
    def test_add(self):
        a = 1
        b = 2
        c = add(a, b)
        assert a + b == c

if __name__ == '__main__':
    unittest.main()
