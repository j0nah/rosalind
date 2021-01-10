class DnaTranscriber:
    def __init__(self, strand):
        self.strand = strand

    def transcribe(self):
        return self.strand.replace("T", "U")