import unittest
from src.fixedXOR import fixedXOR

class TestFixedXOR(unittest.TestCase):
    
    def testEqualStringsResultsInZero(self):
        self.assertEquals(fixedXOR('a', 'a'), '0')

    def testWebsiteExample(self):
        first = "1c0111001f010100061a024b53535009181c"
        second = "686974207468652062756c6c277320657965"
        expected = "746865206b696420646f6e277420706c6179"
        self.assertEquals(fixedXOR(first, second), expected)


