class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        dict1= {}
        for num in nums2:

            while stack and num > stack[-1]:
                dict1[stack.pop()] = num

            stack.append(num)
        while stack:
            dict1[stack.pop()] = -1
        ans = []

        for num in nums1:
            ans.append(dict1[num])
        return ans