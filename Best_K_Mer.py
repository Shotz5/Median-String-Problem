class Best_K_Mer:
    def __init__(self, dna, distance):
        self.dna = dna
        self.distance = distance

    def isNull(self):
        if self.dna == "" or self.distance == -1:
            return 1
        else:
            return 0