class Solution:
    def rob(self, nums):
        
        if len(nums) == 1:
            return nums[0]

        # helper function for normal House Robber
        def helper(arr):
            first = 0
            second = 0

            for money in arr:
                temp = max(first + money, second)
                first = second
                second = temp

            return second

        # case 1: exclude last house
        case1 = helper(nums[:-1])

        # case 2: exclude first house
        case2 = helper(nums[1:])

        return max(case1, case2)