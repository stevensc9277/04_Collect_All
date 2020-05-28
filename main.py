import random

# To do
# Create a list of letters for coffee
tokens = ["C", "O", "F", "E"]
already_got = []

# Pick random letters from a list (looped for testing purposes)
keep_going = ""
while  keep_going == "":
  user = input("Enter to continue: ")
  com = random.choice(tokens)
  already_got.append(com)
  print(already_got)
  keep_going = input("Continue? ")
print("End")
