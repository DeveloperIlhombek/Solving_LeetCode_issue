import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend / divisor == -2147483648:
            return -2147483648
        elif dividend / divisor == 2147483648:
            return 2147483647
        return math.trunc(dividend / divisor)
