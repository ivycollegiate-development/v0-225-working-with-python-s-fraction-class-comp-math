from fractions import Fraction

f0=0.1 + 0.2
print(f0)

f1 = Fraction(3, 4)  # Creates 3/4
print(f1)  # Output: 3/4

# Create a fraction representing 2/5
f2 = Fraction(2, 5)
print(f2)

f3 = Fraction(5)  # Creates 5/1
print(f3)  # Output: 5

f4 = Fraction("7/8")  # Creates 7/8
f5 = Fraction("0.25")  # Creates 1/4 (simplified!)
print(f4)
print(f5)
