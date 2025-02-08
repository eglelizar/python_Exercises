import string
alphabet = list(string.ascii_lowercase) #['a','b','c','d',...]

direction = input ("Type 'encode' to encrypt, type 'decode' to decript: \n").lower()
text = input ("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO: Create a funciton called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    final_text = ""
    for character in original_text.lower() :
        located_in = alphabet.index (character)
        final_text = final_text + alphabet[(located_in + shift_amount)% len(alphabet)]
    return final_text

def decrypt(original_text, shift_amount):
    final_text = ""
    for character in original_text.lower() :
        located_in = alphabet.index (character)
        final_text = final_text + alphabet[(located_in - shift_amount)% len(alphabet)]
    return final_text

result =encrypt(text, shift)
print(f"result: {result}")
result = decrypt(result, shift)
print(f"result: {result}")
        