class toantu(object):
    """docstring for toantu"""

    def __init__(self):
        self.number = 0

    def getvalue(self, temp):
        self.number = temp

    def nhan(self, temp):
        self.number = self.number * temp

    def cong(self, temp):
        self.number = self.number + temp

    def tru(self, temp):
        self.number = self.number - temp

    def chia(self, temp):
        self.number = self.number / temp

    def binhphuong(self):
        self.number = self.number * self.number

    def printnumber(self):
        print (self.number)


result = toantu()
result.getvalue(10)
result.nhan(20)
result.printnumber()
result.chia(10)
result.printnumber()
