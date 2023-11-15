##### This code will be used to create random letters #####

# import needed modules
import string
import random
from PyDictionary import PyDictionary

# initialise variables for vowels 
vowels = "AEIOU"
last_vowel = ""
random_vowels = ""

# initialise variables for consonants
consonants = list(set(string.ascii_uppercase) - set(vowels)) 
last_consonant = ""
random_consonants = ""

#pre-shuffle letters
random.shuffle(consonants)
random.shuffle(list(vowels))

# ask user for number of letters - between 3 and 10
while True :
    try :
        n_ltrs = input("Enter a number between 3 and 10: ")
        if n_ltrs.isdigit() :
            n_ltrs = int(n_ltrs) # change n_ltrs into integer
        else:
            raise ValueError()
        if 3 <= n_ltrs <= 10 :
            break
        raise ValueError()
    except ValueError :
        print("\nInput must be a WHOLE number between 3 and 10.")

# ask user for number of vowels - must not exceed n_ltrs
while True:
    try :
        n_vwls = input(f"\nEnter number of vowels (must not exceed {n_ltrs - 1}): ")
        if n_vwls.isdigit() :
            n_vwls = int(n_vwls) # change n_vwls into integer
        else :
            raise ValueError()
        if 0 <= n_vwls <= n_ltrs - 1 :
            break
        raise ValueError()
    except ValueError :
        print(f"\nInput must be between 0 and {n_ltrs - 1}.")

# generate random vowel letters dyanamically
if 1 <= n_vwls <= 5 :
    random_vowel = random.sample(vowels, n_vwls - 1) # without replacement 
    last_vowel = random.choice(vowels)
elif n_vwls == 0 : # create empty list of vowels if user chooses 0 vowels
    random_vowel = []
    last_vowel = []
else : # avoid errors if user choose more than 5 vowels and using random sampling without replacement 
    random_vowel = random.sample(vowels, 5) 
    last_vowel = random.sample(vowels, n_vwls - 5) # without replacement 

random_vowels = random_vowel + list(last_vowel)

# generate random consonants based on remaining letters needed
random_consonant = random.sample(consonants, n_ltrs - n_vwls - 1) # without replacement 
last_consonant = random.choice(consonants)
random_consonants = random_consonant + list(last_consonant)

# shuffle letters generated
letters_comb = random_vowels + random_consonants
ltrs_list = list(letters_comb)
random.shuffle(ltrs_list)
letters_generated = ' '.join(ltrs_list)

# print letters generated
print(f"\nRandom letters are: {letters_generated}\n")


##### This code ask for answer input and check against dictionary #####

# initiliase dictionary  
dictionary = PyDictionary()

# get user input and check against dictionary

while True :
    try :
        ans = input("Enter your answer: ") # ask for user input
        chk = ans.upper() # put to upper case before checking it against letters generated
        if (set(chk).issubset(ltrs_list)
            and bool(dictionary.meaning(chk, disable_errors = True)) == True) : # disable error as it'll be capture by the exception
                print(f"\nYour answer {chk} is correct!\n")
                break
        else :
            raise ValueError()
    except ValueError :
        print(f"\nYour answer {ans.upper()} is not a valid word. Please try again.\n")