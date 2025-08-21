'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Description: The Fraction class
'''

class Fraction: 

    DEFAULT_VALUE = 1

    def __init__(self, num: int, den: int = DEFAULT_VALUE) -> None:
        self.num = num
        self.den = den if den != 0 else Fraction.DEFAULT_VALUE
    
    def value(self): 
        return self.num / self.den
    
    def gcd(self): 
        a = self.num 
        b = self.den 
        while (b != 0): 
            temp = a
            a = b 
            b = temp % a 
        return a 
    
    def simplify(self): 
        gcd = self.gcd()
        self.num //= gcd 
        self.den //= gcd 
        if self.num == 0: 
            self.den = Fraction.DEFAULT_VALUE 
        elif self.num > 0 and self.den < 0:
            self.num *= -1 
            self.den *= -1 
        
    def is_negative(self): 
        return self.value() < 0
    
    def is_proper(self): 
        return abs(self.num) < abs(self.den)
    
    def clone(self): 
        return Fraction(self.num, self.den)
    
    def __str__(self):
        return str(self.num) + ' / ' + str(self.den)
    
    # TODO: implement the add method that adds another fraction to the callee's fraction, making sure the resulting fraction is simplified
    def add(self, other): 
        
        self.num = self.num*other.den + self.den*other.num
        self.den = self.den*other.den
        
        return self.simplify()
        
if __name__ == '__main__':
    fraction = Fraction(12, -36)
    print(fraction)
    fraction.simplify()
    print(fraction)
    if fraction.is_proper(): 
        print('is proper!')
    print(fraction.value())
    f1 = Fraction(2, 3)
    f2 = Fraction(-8, 10)
    f1 = f1.add(f2)
    print(f1)