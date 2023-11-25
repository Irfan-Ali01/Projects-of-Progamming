terms = int(input("Enter the number of terms: "))
a = 5
b = 6
print(a)
for i in range(1, terms):
  c = a + b
  print(c)
  a = b
  b = c
