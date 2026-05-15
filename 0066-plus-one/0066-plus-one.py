class Solution:
    
    def plusOne(self, digits):
        num = 0

        for d in digits:
            num = num * 10 + d
        num += 1
        ans = []

        for ch in str(num):
            ans.append(int(ch))

        return ans