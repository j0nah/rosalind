import unittest
from count_dna_nucleotides import CountDnaNucleotides

class CountDnaNucleotidesTest(unittest.TestCase):
    def test_count(self):
        test = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        countDnaNucleotides = CountDnaNucleotides(test)
        expected = {
            "A": 20,
            "C": 12, 
            "G": 17,
            "T": 21
        }

        self.assertEqual(expected, countDnaNucleotides.count())

    def test_prettyCount(self):
        test = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        countDnaNucleotides = CountDnaNucleotides(test)
        expected = "20 12 17 21"

        self.assertEqual(expected, countDnaNucleotides.prettyCount())

if __name__ == '__main__':
    unittest.main()