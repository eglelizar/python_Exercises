
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) #4
nr_symbols = int(input(f"How many symbols would you like?\n")) #2
nr_numbers = int(input(f"How many numbers would you like?\n")) #3

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password = ""
# Loop 1 range(0 to len(size  + options sum or nr_letters, symbols and numbers))
#      Pickup what characters are still missing
#       if(they are > 0) nr_letters, nr_symbols, nr_numbers
#           availableCharactersOptions = adding into an array (1,3)
#           chosenOption = random.choice(avaialbleCharactersOptions)
#           password + = GetMeTheArrayCharacter(nr_letters, nr_symbols, nr_numbers)

#           
# method1: GetMetheArrayCharacter(Array_Options)
#   random = random.choice(Array_Options)
#   return Array_Options[random]

def getMeRandomOptionFromArray(array):
    randomLetter = random.choice(array)
    return randomLetter

password = ""

for c in range(0, nr_letters+ nr_symbols + nr_numbers ):
    arrayCharacters = []
    chosenArray = []
    chosenOption = ""
    if (nr_letters > 0):
        arrayCharacters.append ('letters')
    if (nr_symbols > 0):
        arrayCharacters.append ('symbols')
    if (nr_numbers > 0):
        arrayCharacters.append ('numbers')  
    chosenOption = random.choice(arrayCharacters)
    if (chosenOption == "letters"):
        password += getMeRandomOptionFromArray(letters)
        nr_letters = nr_letters -1
    if (chosenOption == "symbols"):
        password += getMeRandomOptionFromArray(symbols)
        nr_symbols = nr_symbols -1  
    if (chosenOption == "numbers"):
        password += getMeRandomOptionFromArray(numbers)
        nr_numbers = nr_numbers -1   

print (f"Your password is: {password}") 



