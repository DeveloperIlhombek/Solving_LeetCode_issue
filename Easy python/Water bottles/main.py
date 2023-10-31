class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        remeinder=numBottles % numExchange
        full=numBottles // numExchange
        result=numBottles
        while remeinder +full >=numExchange:
            result +=full
            remeinder=numBottles %numExchange
            full =numBottles // numExchange
            numBottles=remeinder+full

        return result+1

print(Solution.numWaterBottles(Solution,5,5))
#  BOshqalarni yechimi
# return int(numBottles + (numBottles - 1) / (numExchange - 1))



