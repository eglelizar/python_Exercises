class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        for i in range(len(s)):
            dic = {}
            maxi = max(maxi,lengthOfLongesSubstringRec(s, i, dic))
        return maxi
#dvdf
#abbc
def lengthOfLongesSubstringRec(s,index,dic):
    size = len(dic)
    if (index == len(s) or s[index] in dic):
        return size
    dic[s[index]]=0
    return lengthOfLongesSubstringRec(s, index +1, dic)
s = Solution ()
print(s.lengthOfLongestSubstring("pwwkew"))