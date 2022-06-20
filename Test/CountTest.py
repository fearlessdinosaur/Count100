import unittest

from Source.main import countFromXToY


class CountTest(unittest.TestCase):
    def testCount(self):
        result = countFromXToY(1, 15)
        self.assertEquals(result.split().count("Three"), 4)
        self.assertEquals(result.split().count("Five"), 2)
        self.assertEquals(result.count("ThreeFive"), 1)

    def test_NotANumber(self):
        self.assertRaises(TypeError, countFromXToY, "a", 15)
