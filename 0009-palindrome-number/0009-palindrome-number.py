class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        k = x

        while x > 0:
            digit=x % 10
            rev = rev * 10 +digit
            x //= 10

        return k == rev