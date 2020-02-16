import unittest
from calculator import *

class SimpleTest(unittest.TestCase):

    # Returns True or False.
    def test(self):
        c1=calculator()

        x=c1.Add(3,4)
        self.assertEqual(x,7)
    def test2(self):
        c1=calculator()

        x=c1.Add(3,4)
        self.assertEqual(x,7)


if __name__ == '__main__':
    unittest.main()