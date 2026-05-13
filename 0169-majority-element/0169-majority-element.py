class Solution(object):
    def majorityElement(self, arr):
        count=0
        maz=None
        for num in arr:
            if count==0:
                maz=num
            if num==maz:
                count+=1
            else:
                count-=1
        return maz