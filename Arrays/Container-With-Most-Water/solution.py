class Solution:
    def containerMostWater(height):
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            width=right-left
            area=width*min(height[left],height[right])
            max_area=max(area,max_area)
            if height[left]<height[right]:
                left+=1
            elif height[right]<height[left]:
                right-=1
            else:
                left+=1
        return max_area