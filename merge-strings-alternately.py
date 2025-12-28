from collections import deque

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lst1, lst2 = deque(word1), deque(word2)
        res = []

        while lst1 and lst2:
            res.append(lst1.popleft())
            res.append(lst2.popleft())

        if lst1:
            res += lst1
        elif lst2:
            res += lst2

        return "".join(res)
