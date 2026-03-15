# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# { "a", "b"} //  set

class LongestSubstring():
    def lengthOfLongestSubstring(self, s):
        ind = 0
        dicSub = set()
        dicSubs = {}
        maxLen = 0
        maxStr = ''
        while (ind < len(s)):
            currentLen = len(dicSub)
            dicSub.add(s[ind])
            if currentLen == len(dicSub):
                substring = ''
                n = 0
                while (n < len(dicSub)):
                    substring = substring + dicSub.pop()
                if (maxLen < currentLen):
                    maxLen = currentLen 
                    maxStr = substring
                dicSub.clear()
            else:
                ind = ind+1
        substring = ''
        if len(dicSub) > 0 and len(dicSub)  > maxLen:
            n = 0
            while (n < len(dicSub)):
                substring = substring + dicSub.pop()
            maxLen = len(substring)
            maxStr = substring
        print('max string ' , maxStr)      
        return maxLen

string = 'dvdf'
obj = LongestSubstring()
print(obj.lengthOfLongestSubstring(string))