# array 10 2 3 4 5 9 10
# new array

class Solution:
    def merge(self, nums1, m, nums2, n):
        i =0 
        i1 =0
        i2=0
        z = 0
        nums =[]
        for i in range (0, len(nums1)):
            if nums1[i1] <=  nums2[i2] and nums1[i1] > 0:
                print ("appending ", nums1[i1])
                nums.append(nums1[i1])
                i1 = i1 + 1
                z = z+1
                continue
            else:
                nums.append( nums2[i2])
                i2 = i2 + 1
                z = z+1
        print(nums)
        nums1 = nums
             
nums1 = [1,2,3,3,0,0,0]
m = 4
nums2 = [2,6,6]
n =3
S = Solution ()
S.merge(nums1, m, nums2, n)
#print (nums1)