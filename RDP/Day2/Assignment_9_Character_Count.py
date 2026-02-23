# Assignment 9 Character Count Write a
# program that takes a string as input and counts
# the number of occurrences of a specific character
# entered by the user.

string_input = input("Enter a string: ")
character_input = input("Enter a character: ")



# for i in range(len(string_input)):
#     if string_input[i] == character_input:
#         count += 1

occ = string_input.count(character_input)
if occ == 0:
    print("The character isn't present in the string")
elif occ == 1:
    print(f"The character '{character_input}' occurs {occ} time")
else:
    print(f"The character '{character_input}' occurs {occ} times")


