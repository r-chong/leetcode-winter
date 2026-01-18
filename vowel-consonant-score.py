import math

class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = set(('a','e','i','o','u'))
        v = 0
        c = 0
        score = 0
        
        for char in s:
            if char.isalpha() and char in vowels:
                v += 1
            elif char.isalpha():
                c += 1

        if c > 0:
            score = math.floor(v / c)
        
        return score