from fractions import Fraction
import sys

a = Fraction(1,3)
c = 1/3
b = c*3

print(b)
print(sys.getsizeof(a))
print(sys.getsizeof(b))