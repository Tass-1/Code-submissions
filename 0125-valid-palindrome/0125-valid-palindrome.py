class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = ""
        for i in range(len(s)):
            curr = s[i]
            if curr.isalnum():
                b += curr
        left = 0
        right = len(b)-1
        print(b)
        while left <= right:
            if b[left].lower() != b[right].lower():
                return False
            left += 1
            right -= 1
        return True