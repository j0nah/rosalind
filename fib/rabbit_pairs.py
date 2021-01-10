import unittest

class RabbitPairs:
    def __init__(self, numMonths, numPairs):
        self.numPairs = numPairs
        self.numMonths = numMonths
        self.currentPairs = 1
        self.currentPregnant = 0
    
    def totalPairs(self):
        for i in range(0,self.numMonths-1):
            tmpPairs = self.currentPairs
            tmpPregnant = self.currentPregnant
            self.currentPregnant = tmpPairs
            self.currentPairs = tmpPairs + tmpPregnant*self.numPairs
        
        return self.currentPairs


class RabbitPairsTest(unittest.TestCase):
    def test_totalPairs(self):
        rp = RabbitPairs(5,3)
        self.assertEqual(19, rp.totalPairs())

