class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1
        maxarea=0
        while l<r:
            b=r-l
            h=min(height[l],height[r])
            maxarea=max(maxarea,b*h)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxarea
        