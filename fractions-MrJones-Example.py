from fractions import Fraction

f1 = Fraction(3, 4)  # Creates 3/4
print(f1)  # Output: 3/4

# Create a fraction representing 2/5
f2 = Fraction(2, 5)
print(f2)

# Method 2: From a Single Integer
f3 = Fraction(5)  # Creates 5/1
print(f3)  # Output: 5

#Method 3: From a String
f4 = Fraction("7/8")  # Creates 7/8
f5 = Fraction("0.25")  # Creates 1/4 (simplified!)
print(f4)
print(f5)
#Your Turn:
# Create a fraction from the string "3/10"
f6 = Fraction("3/10")

# Create a fraction from the decimal string "0.5"
f7 = Fraction("0.5")

#Method 4: From a Float (Use Carefully!)
f8 = Fraction(0.75)  # Creates 3/4
print(f8)
