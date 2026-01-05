class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        content = 0
        
        greed = sorted(g)
        j = 0
        cookies = sorted(s)
        max_cookies = len(cookies)

        for c in greed:
            while j < max_cookies and cookies[j] < c:
                j += 1  # skip cookies that are too small

            if j < max_cookies:
                content += 1
                j+= 1

        return content

# divergences:
# recall that wecan only give each child ONE cookie
# so there are cases:
# lowest of g == lowest of s: then give their minimum contentness
# lowest of g < lowest of s: then give greater than their minimum contentness
# lowest of g > lowest of s: then skip all cookies up until g <= lowest of s <-- was missing this case