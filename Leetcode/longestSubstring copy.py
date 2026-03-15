# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# { "a", "b"} //  set

class LongestSubstring():
    def lengthOfLongestSubstring(self, s):
        ind = 0
        maxCharacters = 0
        while (ind < len(s)):
            sInd = ind
            charactersCounter = 0
            dict = set()
            while (sInd < len(s)):
                previousCounter= len(dict)
                dict.add(s[sInd])
                if (len(dict) == previousCounter):
                    break
                charactersCounter = charactersCounter +1
                sInd = sInd +1
            if (maxCharacters< charactersCounter):
                maxCharacters = charactersCounter
                print('String ' , s[ind:sInd])
            ind = ind +1
        return maxCharacters


string = 'bbbbb'
obj = LongestSubstring()
print(obj.lengthOfLongestSubstring(string))