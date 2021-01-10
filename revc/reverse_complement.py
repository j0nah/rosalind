class ReverseComplement:
    def __init__(self, strand):
        self.strand = strand
        self.nucelotideMapping = {
            "G": "C",
            "C": "G",
            "A": "T",
            "T": "A"
        }

    def reverseComplement(self):
        rcStrand = ""
        for n in self.strand:
            rcStrand += self.nucelotideMapping[n]

        return rcStrand[::-1]
        
