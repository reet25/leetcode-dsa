class Solution:
    def sortedSquares(nums):
        squares=[0]*len(nums)
        left=0
        right=len(nums)-1
        pos=len(nums)-1
        while left<=right:
            if (abs(nums[left]))<=(abs(nums[right])):
                squares[pos]=nums[right]*nums[right]
                right-=1
                pos-=1
            else:
                squares[pos]=nums[left]*nums[left]
                left+=1
                pos-=1
        return squares