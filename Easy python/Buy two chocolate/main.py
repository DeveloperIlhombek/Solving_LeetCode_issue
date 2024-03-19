class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        sort_prices=sorted(prices)
        if money >=sum(sort_prices[:2:]):
            return money-sum(sort_prices[:2:])
        return money

print(Solution.buyChoco(Solution,[1,10,7],7))
