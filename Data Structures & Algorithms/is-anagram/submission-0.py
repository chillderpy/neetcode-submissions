class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}
        for ch in s:
            if ch not in h1:
                h1[ch] = 1
            else:
                h1[ch] += 1
        for ch in t:
            if ch not in h2:
                h2[ch] = 1
            else:
                h2[ch] += 1

        return h1 == h2