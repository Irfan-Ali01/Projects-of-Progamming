num = int(input("Enter a non-negative integer: "))
factorial = 1
n = num
while n > 0:
  factorial = factorial * n
  n = n - 1
print(f"The factorial of {num} is {factorial}")
