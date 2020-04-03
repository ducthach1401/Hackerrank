class stringS(object):
    """docstring for stringS"""

    def __init__(self):
        self.s = ""

    def getString(self, temp):
        self.s = temp

    def caps(self):
        self.s = self.s.upper()

    def printS(self):
        print (self.s)


result = stringS()
result.getString("abc")
result.caps()
result.printS()
