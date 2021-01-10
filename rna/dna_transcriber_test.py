import unittest
from dna_transcriber import DnaTranscriber

class DnaTranscriberTest(unittest.TestCase):
    def test_transcribe(self):
        input = "ATCG"
        res = DnaTranscriber(input)
        expected = "AUCG"
        self.assertEqual(expected, "AUCG")
