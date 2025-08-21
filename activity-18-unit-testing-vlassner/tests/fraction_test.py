'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Description: The FractionTestCase class
'''

import unittest 
from fraction import Fraction

class FractionTestCase(unittest.TestCase): 

    def test_num_1_den_1(self):
        f = Fraction(1)
        self.assertEqual(1, f.num)
        self.assertEqual(1, f.den)
        self.assertFalse(f.is_proper())

    def test_denominator_one(self): 
        f = Fraction(-3)
        self.assertEqual(-3, f.num)
        self.assertEqual(1, f.den)
        f = Fraction(3)
        self.assertEqual(3, f.num)
        self.assertEqual(1, f.den)
        f = Fraction(1, 1)
        self.assertEqual(1, f.num)
        self.assertEqual(1, f.den)
        f = Fraction(-3, 1)
        self.assertEqual(-3, f.num)
        self.assertEqual(1, f.den)
        f = Fraction(3, 1)
        self.assertEqual(3, f.num)
        self.assertEqual(1, f.den)    

    # TODO
    def test_denominator_zero(self):
        f = Fraction(1,0)
        self.assertEqual(1, f.num)
        self.assertEqual(Fraction.DEFAULT_VALUE,f.den)

    # TODO
    # pre-condition: a fraction 12/36 is instantiated
    # post-condition: numerator is 12; denominator is 36; the fraction is proper; its value is 0.333...
    def test_12_over_36_no_simplification(self):
        f = Fraction(12,36)
        self.assertEqual(12,f.num)
        self.assertEqual(36,f.den)
        self.assertTrue(f.is_proper)
        self.assertAlmostEqual(0.333333, f.value(), 3)
 
    # TODO
    # pre-condition: the fraction 12/36 is simplified
    # post-condition: numerator is 1; denominator is 3; the fraction is still proper and its value is the same; 
    def test_12_over_36_with_simplification(self):
        f = Fraction(12,36)
        f.simplify()
        self.assertEqual(1,f.num)
        self.assertEqual(3,f.den)
        self.assertTrue(f.is_proper)
        self.assertAlmostEqual(0.333, f.value, 3)

    # TODO
    def test_36_over_12(self):
        f = Fraction(36,12)
        self.assertEqual(36, f.num)
        self.assertEqual(12, f.den)
        self.assertEqual(3, f.value(), 3)


    # TODO 
    # pre-condition: fraction 2/3 (callee) and 3/5 (parameter) are instantiated
    # post-condition: the callee fraction (2/3) becomes 19/15; fraction 3/5 remains unchanged
    def test_2_over_3_add_3_over_5(self):
        f1 = Fraction(2,3)
        f2 = Fraction(3,5)
        f1.add(f2)
        self.assertEqual(19, f1.num)
        self.assertEqual(15, f1.den)
        self.assertEqual(3, f2.num)
        self.assertEqual(5, f2.den)


if __name__ == '__main__':
    unittest.main()