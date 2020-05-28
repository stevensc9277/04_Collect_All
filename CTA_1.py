import random

# To do
# Create a list of letters for coffee
tokens = ["C", "O", "F", "E"]
already_got = []

# Pick random letters from a list (looped for testing purposes)
for item in range(0, 5):
  user = input("Enter to continue: ")
  com = random.choice(tokens)
  already_got.append(com)
  print(already_got)
  print()
