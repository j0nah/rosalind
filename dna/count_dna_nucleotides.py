import collections

# A string is simply an ordered collection of symbols selected from some alphabet
# and formed into a word; the length of a string is the number of symbols that it contains.
class CountDnaNucleotides:
    def __init__ (self, dnaString):
        self.dnaString = dnaString
        self.count_a = 0
        self.count_c = 0
        self.count_t = 0
        self.count_g = 0

    def count(self):
        return collections.Counter(list(self.dnaString))

    def prettyCount(self):
        res = self.count()
        return "{} {} {} {}".format(res["A"], res["C"], res["G"], res["T"])