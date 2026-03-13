class Solution:
    def twoSum(self, nums, target):
        result = []
        for i in range (len(nums)):
            complement = target - nums[i]
            if complement in nums:
                complementIndex = nums.index(complement) 
                
                if (i == complementIndex):
                    continue
                result.append(i)                
                result.append(complementIndex)
                return result

num = [3,2,4]
target = 6
c = Solution()
c.twoSum(num, target);
print (c)