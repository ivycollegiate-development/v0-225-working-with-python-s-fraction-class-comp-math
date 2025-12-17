from fractions import Fraction
def get_fraction(prompt):
while True:
try:
num = int(input(f"{prompt} - Enter numerator: "))
den = int(input(f"{prompt} - Enter denominator: "))
return Fraction(num, den)
except ZeroDivisionError:
print("❌ Error: Denominator cannot be zero. Try again.")
except ValueError:
print("❌ Error: Please enter valid integers. Try again.")

def get_operation():
valid_ops = ['+',
'-'
,
'*'
, '/']
while True:
op = input("Enter operation (+, -, *, /): ")
if op in valid_ops:
return op
else:
print(f"❌ Invalid operation. Choose from: {valid_ops}")
def calculate(frac1, frac2, operation):
if operation == '+':
return frac1 + frac2
elif operation == '-':
return frac1 - frac2
elif operation == '*':
return frac1 * frac2
elif operation == '/':
return frac1 / frac2
# Main program
print("=== Fraction Calculator ===\n")
fraction1 = get_fraction("First fraction")
fraction2 = get_fraction("Second fraction")
op = get_operation()
result = calculate(fraction1, fraction2, op)
print(f"\n✓ Result: {fraction1} {op} {fraction2} = {result}")