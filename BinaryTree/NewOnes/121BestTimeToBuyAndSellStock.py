import sys
class Solution:
    def maxProfit(self, prices: int) -> int:
        #print ("-----------------------")
        min = sys.maxsize
        maximumProfit = 0

        for i in range (0, len(prices)-1):
            max = 0
            if (prices [i] < min):
                min = prices[i]
            #print("New min: ", min)
            k = i +1

            if (prices[k]> max ):
                max = prices [k]
                #print("New max: ", max)
                if (max - min > maximumProfit):
                    maximumProfit = max -min       
        return  maximumProfit
    
m = Solution()
print(m.maxProfit([7,1,2,6,5,10]))
print(m.maxProfit([7,1,1,1]))
print(m.maxProfit([7,1,5,3,6,4]))
print(m.maxProfit([2,9,5]))
                    