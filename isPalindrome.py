from unittest import TestCase
def FindIfAStringIsPalindrome(s):
    print (s)

    lastIndex =len(s)-1
    finalChar = s[lastIndex]
    currentIndex = 0

    for singleChar in s:
        if (singleChar.lower() != finalChar.lower()):
            return False
        lastIndex -= 1
        finalChar = s[lastIndex]
        currentIndex +=1
    
    if (lastIndex < 0 and currentIndex == len(s)):
        return True
    
    return False

print(FindIfAStringIsPalindrome("Anita lava la tina".replace(' ', '')))