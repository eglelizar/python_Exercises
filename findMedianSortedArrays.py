def findMedianSortedArrays( nums1, nums2):
        #result 1 2 3
        #indA 0 1
        #indB 0 1
        #totalNumbers 3
        #i 0 1 2
        #nums1 1 3
        #nums2 2
        result = []
        indA = 0
        indB = 0
        totalNumbers = len(nums1) + len(nums2)
        i = 0
        #1. Doing merge of both arrays into result
        while i < totalNumbers:
            if  (indA < len(nums1) and (indB == len(nums2) or nums1[indA] <= nums2[indB])):
                result.append(nums1[indA])
                indA += 1
            elif(indB < len(nums2)):
                result.append(nums2[indB])
                indB += 1
            i+=1
        #2. Calculating the median
        if(totalNumbers %2 == 0):
            return float((result [int(totalNumbers /2 -1)] + result[int(totalNumbers /2)]) /2)
        return float(result[int(totalNumbers / 2)])

nums1 = [1,2] 
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2))