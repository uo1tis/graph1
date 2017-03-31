class Arc:
    def __init__(self,I,J,weight = 1):
        self.I = I
        self.J = J
        self.weight = weight
    def __str__(self):
        return '({} {} {})'.format(self.I, self.J, self.weight)
    def getI(self):
        return int(self.I)
    def getJ(self):
        return int(self.J)
    def getWeigh(self):
        return int(self.weight)