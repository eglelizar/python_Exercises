def myAtoi(str):
    #1. for O(n)
    signed = 1
    alreadySigned = False
    alreadyWhiteSpaces = False
    finalNumber = int()
    for c in str:
        if (c == ' ' and finalNumber ==0 and  alreadyWhiteSpaces==False ):
            continue
        alreadyWhiteSpaces=True        
        if (c == '-' and alreadySigned == False):
            signed = -1
            alreadySigned = True
            continue
        if(c == '+' and alreadySigned == False):
            alreadySigned = True
            continue
        if (alreadySigned == True and (c == '-' or c == '+') and finalNumber == 0):
            return 0
        if(c.isdigit() is not True):
            break
        finalNumber = finalNumber * 10 + int(c) 
        if(finalNumber ==0):
            alreadySigned = True      
    finalNumber *= signed
    limit = pow(2, 31)
    if (finalNumber >limit-1):
        return limit-1
    if (finalNumber < -limit):
        return -limit
    return finalNumber

print(myAtoi("-5-"))
        