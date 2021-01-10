import unittest
from reverse_complement import ReverseComplement

class ReverseComplementTest(unittest.TestCase):
    def test_reverseComplement(self):
        rc = ReverseComplement("AAAACCCGGT")
        expected = "ACCGGGTTTT"
        actual = rc.reverseComplement()
        self.assertEqual(expected, actual)