class Solution(object):
    def separateDigits(self, nums):

        nl = []

        for i in nums:

            for digit in str(i):
                nl.append(int(digit))

        return nl