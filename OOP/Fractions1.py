class Fraction:

    def __init__(self, num, den):
        self.numerator = num
        self.denominator = den

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def simplify(self):
        a = self.numerator
        b = self.denominator
        c = a % b
        while c != 0:
            a = b
            b = c
            c = a % b

            self.numerator //= b
            self.denominator //= b

    def simplified(self):
        new_fraction = Fraction(self.numerator, self.denominator)
        new_fraction.simplify()
        return new_fraction

    def __eq__(self, other_fraction):
        new_fraction1 = Fraction(self.numerator, self.denominator)
        new_fraction2 = Fraction(other_fraction.numerator, other_fraction.denominator)
        new_fraction1.simplify()
        new_fraction2.simplify()
        
        return (new_fraction1.numerator == new_fraction2.numerator) and (new_fraction1.denominator == new_fraction2.denominator)

    def __ne__(self, other_fraction):
        new_fraction1 = Fraction(self.numerator, self.denominator)
        new_fraction2 = Fraction(other_fraction.numerator, other_fraction.denominator)
        new_fraction1.simplify()
        new_fraction2.simplify()

        return (new_fraction1.numerator != new_fraction2.numerator) or (new_fraction1.denominator != new_fraction2.denominator)


    def __gt__(self, other_fraction):
        new_fraction1 = Fraction(self.numerator, self.denominator)
        new_fraction2 = Fraction(other_fraction.numerator, other_fraction.denominator)
        new_fraction1.simplify()
        new_fraction2.simplify()
        self.numerator*self.other.denominator>self.other_numerator*self.denominator
        


    def __add__(self, other_fraction):
        denom = self.denominator * other_fraction.denominator
        num = self.numerator * other_fraction.denominator + other_fraction.numerator * self.denominator
        sum_fraction = Fraction(num, denom).siplified()


        return sum_fraction

fraction1 = Fraction(21,36)
print(fraction1)

fraction2 = fraction1.simplified()
print(fraction2)