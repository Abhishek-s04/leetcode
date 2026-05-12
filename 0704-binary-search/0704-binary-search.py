class Solution(object):
    def search(self, arr, target):
        l=0
        h=len(arr)-1
        while l<=h:
            mid=(l+h)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                l=mid+1
            else:
                h=mid-1
        return -1