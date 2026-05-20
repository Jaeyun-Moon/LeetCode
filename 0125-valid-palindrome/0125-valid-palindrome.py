class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        strs = [char for char in s if char.isalnum()]
        return strs[::] == strs[::-1]