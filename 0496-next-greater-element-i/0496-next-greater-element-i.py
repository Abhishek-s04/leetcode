class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        new = []
        for i in nums1:
            found = False
            ans = -1
            for j in nums2:
                if j == i:
                    found = True
                elif found and j > i:
                    ans = j
                    break
            new.append(ans)
        return new