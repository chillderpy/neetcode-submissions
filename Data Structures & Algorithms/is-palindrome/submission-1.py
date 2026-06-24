class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            left = s[l]
            right = s[r]
            if not left.isalnum():
                l += 1
            elif not right.isalnum():
                r -= 1
            else:
                left = left.lower()
                right = right.lower()
                if left != right:
                    return False
                l += 1
                r -= 1
        
        return True