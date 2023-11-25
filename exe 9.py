num = int(input("Enter a positive integer: "))
a = num
reverse = 0
while num > 0:
  digit = num % 10
  reverse = reverse * 10 + digit
  num = num // 10
if a == reverse:
  print(f"{a} is a palindrome")
else:
  print(f"{a} is not a palindrome")
