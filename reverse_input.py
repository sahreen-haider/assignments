# program to reverse a given word which was given as input from the user


word = input("Input a word to reverse: ")      # using the input() fn for the variable "word"

for _ in range(len(word) - 1, -1, -1):
  print(word[_], end="")
print("\n")