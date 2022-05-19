class ComplexNumber:

    def __init__(self,re,im):
        self.re = int(re)
        self.im =int(im)

    def mod(self):
        return (self.re**2 + self.im**2)**0.5

    def __add__(self,other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __sub__(self,other):
        return ComplexNumber(self.re - other.re, self.im - other.im)

    def __mul__(self,other):
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + self.im * other.re
        return ComplexNumber(re, im)

    def __lt__(self,other):
        if self.mod() < other.mod():
            return True
        return False
    def __gt__(self,other):
        if self.mod() > other.mod():
            return True
        return False
    def __eq__(self,other):
        if self.mod() == other.mod():
            return True
        return False

    def __str__(self):
        if self.im < 0:
            return str(self.re) + str(self.im) + "i"
        else:
            return str(self.re) + "+" + str(self.im) + "i"