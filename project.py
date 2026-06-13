base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent (positive integer): "))

result = 1.0
count = exponent

while count > 0:
    result *= base
    count = count - 1

print(f"{base} raised to the power of {exponent} is: {result}")

