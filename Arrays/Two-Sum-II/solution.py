class Solution:
    def TwoSumII(numbers,target):
        left=0
        right=len(numbers)-1
        while left<right:
            add=numbers[left]+numbers[right]
            if add>target:
                right-=1
            elif add<target:
                left+=1
            else:
                return [left+1,right+1]