from math import isqrt 

class Solution: 
    def sumFourDivisors(self, nums: List[int]) -> int: 
        total = 0 
        for n in nums: 
            total += self.processNum(n) 

        return total 

        def processNum(self, n): 
            sqrt = isqrt(n) 
            x = 2 
            count = 2
            sum = 1 + n
            
            while x <= sqrt:
                if n % x == 0: 
                    if (n // x == x): 
                        # it's a square so only add one divisor (no duplicates)
                        count += 1 
                        total += x 
                    else: 
                        count += 2 
                        total += x + n // x # add both 

                x += 1

            return total if count == 4 else 0 

# divergences: 
# thought the while loop was to halfway not sqrtx
# didn't keep a running sum in processNum
# must use <= sqrt not < sqrt (in case of perfect square)
# A further optimization is that a perfect square being a divisor rules it out as it makes the # of divisors odd