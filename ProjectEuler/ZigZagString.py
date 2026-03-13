import collections
#PAHNAPLSIIG  Y  I  R
#012345678910 11 12 13
#convertedString P
#ascendingOrder True 
# i 0 1
#numRows 3
# module 
# newIndex 0 
def convert(s, numRows):
    if (numRows == 1):
        return s
    lists = collections.defaultdict(list)
    ascendingOrder = True
    indexLists = 0
    for i in range(len(s)):
        lists[indexLists].append(s[i])
        if (ascendingOrder == True):
            if (indexLists == numRows -1):
                ascendingOrder = False
                indexLists -= 1
            else:
                indexLists +=1
        else:
            if(indexLists == 0):
                ascendingOrder = True
                indexLists += 1
            else:
                indexLists -= 1     
    convertedString = ""
    for l in lists:
        for ll in lists[l]:
            convertedString+=ll
    return convertedString

print(convert("PAYPALISHIRING",3))


    
