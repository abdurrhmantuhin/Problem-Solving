class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert integer to string
        s = str(x)
        # check if string is equal to its reverse
        return s == s[::-1]

w = Solution()
print(w.isPalindrome(122)) # False
print(w.isPalindrome(121)) # True
print(w.isPalindrome("level")) # True
