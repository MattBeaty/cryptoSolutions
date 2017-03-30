import unittest
from src.hexToBase64 import hexToBase64

class TestHexToBase64(unittest.TestCase):

    def testOneByteIsPadded(self):
        self.assertEqual(hexToBase64("4d"), "TQ==")

    def testTwoBytesArePadded(self):
        self.assertEqual(hexToBase64("4d61"), "TWE=")

    def testThreeBytesAreFullBase64String(self):
        self.assertEqual(hexToBase64("4d616e"), "TWFu")

    def testSixBytesAreTwoBase64Strings(self):
        self.assertEqual(hexToBase64("49276d206b69"), "SSdtIGtp")

    def testPaddingOnExtraByte(self):
        self.assertEqual(hexToBase64("49276d206b694d"), "SSdtIGtpTQ==")

    def testPaddingOnTwoExtraBytes(self):
        self.assertEqual(hexToBase64("49276d206b694d61"), "SSdtIGtpTWE=")

    def testWebsiteTestPasses(self):
        self.assertEqual(hexToBase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"), "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")

if __name__ == '__main__':
    unittest.main()
