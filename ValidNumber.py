# negative integer or decimal _e_ negative integer
#integer _._ integer
#-integer or -decimal
# not valid caracters
def isNumber (s):
    isSigned = False
    isExponential = False
    isDecimal = False
    allowWhitespaces = True
    finalNumber = ''
    previousChar = ''
    if s == ' ':
        return False
    for c in s:
        if c == ' ' and (allowWhitespaces == True and finalNumber != '.' and finalNumber != 'e' or isNumber(finalNumber)):
            previousChar = c
            continue
        if((c == '+' or c == '-') and isSigned == False):
            isSigned = True
        elif (c == '.' and isDecimal == False and isExponential == False):
                isDecimal = True
        elif (c == 'e'and isExponential == False and finalNumber != ''):
            isExponential = True
            isSigned = False
        elif (c.isdigit()==False):
            return False
        elif (finalNumber != '' and previousChar == ' '):
            return False
        finalNumber += c

        allowWhitespaces = False
    if ((finalNumber and finalNumber[-1]== 'e' ) or not finalNumber or (finalNumber and len(finalNumber) == 1 and finalNumber[-1]== '.')):
        return False
    return True

print (isNumber(".e1"))
        
