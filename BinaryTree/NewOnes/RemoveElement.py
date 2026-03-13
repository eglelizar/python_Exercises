class Solution:
    def removeElement(self, nums, val: int) -> int:
        copy = nums.copy()
        copy_ind = 0
        equal = 0
        for k in copy:
            print (nums)
            if (k == val):
                equal = equal +1
            else:
                nums[copy_ind] = k
                copy_ind = copy_ind +1
        for v in range(copy_ind, len(nums)):
            nums[v] = 0
        return equal
sol = Solution()
array = [0,1,2,2,3,0,4,2]
val = 2
print(sol.removeElement(array, val))
print (array)
