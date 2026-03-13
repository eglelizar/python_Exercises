import sys
class Solution:
    memoization = {}

    def getMaxProfitWithCurrInd (self,prices, currInd):

        valToEvaluate = prices [currInd]

        if valToEvaluate in self.memoization:
            print ("used memoization ", valToEvaluate)
            return self.memoization [valToEvaluate]
 
        fromInd = currInd + 1
        max = 0

        for i in range (fromInd, len(prices)):
            if (valToEvaluate < prices [i] and  prices[i] > max):  
                max = prices[i]
        
        #print ("max to Evaluate ", max, " val to eval: ", valToEvaluate)
        self.memoization[valToEvaluate] =  max - valToEvaluate

        return max - valToEvaluate
    

    def maxProfit(self, prices: int) -> int:
        self.memoization = {}
        maxProfit = 0

        for i in range(0, len(prices)):
            maxInThisOption = self.getMaxProfitWithCurrInd(prices, i)
            if (maxInThisOption > maxProfit):
                maxProfit = maxInThisOption

        return  maxProfit
    
m = Solution()
print(m.maxProfit([7,1,2,6,5, 7, 10]))  #9
print(m.maxProfit([7,1,1,1]))       #0
print(m.maxProfit([7,1,5,3,6,4]))   #5
print(m.maxProfit([2, 5 ,9]))      #7

                    