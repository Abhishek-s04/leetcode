class Solution(object):

    def searchRange(self, nums, target):

        ans = []

        for i in range(len(nums)):

            if nums[i] == target:
                ans.append(i)

        if len(ans) > 0:
            return [ans[0], ans[-1]]

        return [-1, -1]
