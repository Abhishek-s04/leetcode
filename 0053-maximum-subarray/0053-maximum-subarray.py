class Solution(object):
    def maxSubArray(self, nums):
        current_sum=nums[0]
        _3sum=nums[0]
        for i in range(1,len(nums)):
            current_sum=max(nums[i],current_sum+nums[i])
            _3sum=max(_3sum,current_sum)
        return _3sum
        