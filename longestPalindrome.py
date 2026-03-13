def longestPalindrome(s):
    if (len(s) <= 1 or isPalindrome(s)):
        return s
    maxString = s[0]
    for startIndex in range(len(s)):
        for endIndex in range(startIndex +2, len(s)+1):
            strToEvaluate = s[startIndex: endIndex]
            print(strToEvaluate)
            if(len(strToEvaluate) > len(maxString) and (isPalindrome(strToEvaluate))):
                maxString = strToEvaluate
    return maxString


def longestPalindromeRec3(s):
    if (len(s) <= 1 or isPalindrome(s)):
        return s
    maxString = s[0]
    #Edge cases
    #dic = {}
    #for c in range (len(s)):
    #    if s[c] not in dic:
    #        dic[s[c]] = []
    #    dic[s[c]].append(c)
    #isPair = (len(s)%2== 0)

    for lengthStr in range(len(s), 1, -1):
        startIndex =0
        while startIndex + lengthStr < len(s) +1:
            strToEvaluate = s[startIndex:startIndex+lengthStr]
            print(strToEvaluate)
            if(isPalindrome(strToEvaluate)):
                #maxString = strToEvaluate
                return strToEvaluate
            startIndex +=1
        if(len(maxString)>1):
            break
    return maxString


# def longestPalindrome2(s):
#     maxxi  = ""
#     for i in range(len(s)):
#         cad = longestPalindromeRec (s, i, 1)
#         if (len(cad)>len(maxxi)):
#             maxxi = cad
#     return maxxi 

# def longestPalindromeRec2(s, startIndex, length):
#     #1. Stop when we have reached out
#     position = startIndex + length
#     if (len(s) < position):
#         return ""
#     #2. Get string to Evaluate
#     strToEvaluate = s[startIndex: position]
#     #3. Ask child for his status
#     child = longestPalindromeRec(s, startIndex, length +1)
#     #4. Check if I am palindrome
#     if (isPalindrome(strToEvaluate) and len(strToEvaluate)>len(child)):
#         return strToEvaluate
#     return child
    
    
def isPalindrome (str):
    initial = 0
    final = len(str) -1
    if (str[initial] != str[final]):
        return False
    while(initial <= final and str[initial] == str[final]):
        initial += 1
        final -= 1
    if (initial >= final):
        return True
    return False

print(longestPalindrome ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))