class Solution(object):

    def searchRange(self, nums, target):

        first = -1
        last = -1
        # Find first occurrence
        l = 0
        h = len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                first = mid
                h = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        # Find last occurrence
        l = 0
        h = len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                last = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return [first, last]