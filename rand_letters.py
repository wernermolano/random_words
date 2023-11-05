##### This code will be used to create random letters #####

# import needed modules
import string
import random

# initialise variables for vowels 
random_vowels = ""
vowels = "AEIOU"

# initialise variables for consonants
consonants = list(set(string.ascii_uppercase) - set(vowels)) 
random_consonants = ""

# ask user for number of letters - between 3 and 9
while True:
    try:
        n_ltrs = input("Enter a number between 3 and 9: ")
        if n_ltrs.isdigit():
            n_ltrs = int(n_ltrs) # change n_ltrs into integer
        else:
            raise ValueError()
        if 3 <= n_ltrs <= 9:
            break
        raise ValueError()
    except ValueError:
        print("\nInput must be a WHOLE number between 3 and 9.")

# ask user for number of vowels - must not exceed n_ltrs
while True:
    try:
        n_vwls = input(f"\nEnter number of vowels (must not exceed {n_ltrs}): ")
        if n_vwls.isdigit():
            n_vwls = int(n_vwls) # change n_vwls into integer
        else:
            raise ValueError()
        if 0 <= n_vwls <= n_ltrs:
            break
        raise ValueError()
    except ValueError:
        print(f"\nInput must be between 0 and {n_ltrs}.")

# generate random vowel letters dyanamically 
for i in range(n_vwls) : 
    random_vowel = random.choice(vowels)
    random_vowels += random_vowel

# generate random consonants based on remaining letters needed
for i in range(n_ltrs - n_vwls) : 
    random_consonant = random.choice(consonants)
    random_consonants += random_consonant

# shuffle letters generated
letters_comb = random_vowels + random_consonants
ltrs_list = list(letters_comb)
random.shuffle(ltrs_list)
letters_generated = ' '.join(ltrs_list)

# print letters generated
print(f"\nRandom letters are: {letters_generated}")