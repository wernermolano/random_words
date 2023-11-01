##### This code will be used to create random letters #####

# import needed modules
import string
import random

# initialise variables needed
random_vowels = ""
vowels = "AEIOU"

# ask user for number of letters - between 3 and 9
while True:
    try:
        n_ltrs = input("Enter a number between 3 and 9: ")
        if n_ltrs.isdigit():
            n_ltrs = int(n_ltrs)
        else:
            raise ValueError()
        if 3 <= n_ltrs <= 9:
            break
        raise ValueError()
    except ValueError:
        print("Input must be a WHOLE number between 3 and 9.")

# ask user for n umber of vowels - must not exceed n_ltrs
while True:
    try:
        n_vwls = input(f"Enter number of vowels (must not exceed {n_ltrs}): ")
        if n_vwls.isdigit():
            n_vwls = int(n_vwls)
        else:
            raise ValueError()
        if 0 <= n_vwls <= n_ltrs:
            break
        raise ValueError()
    except ValueError:
        print(f"Input must be between 0 and {n_ltrs}.")


# generate random letters dyanamically 
for i in range(n_ltrs) : # change n_ltrs into integer
    random_letter = random.choice(string.ascii_uppercase)
    random_letters += random_letter

print(f"Random letters are: {random_letters}")