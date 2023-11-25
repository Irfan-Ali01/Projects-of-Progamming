string = input("Enter a string: ")
vowels = 0
for char in string:
  char = char.lower()
  if char in "aeiou":
    vowels = vowels + 1
print(f"The number of vowels in {string} is {vowels}")
