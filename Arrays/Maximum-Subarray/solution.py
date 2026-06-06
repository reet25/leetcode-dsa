class Solution:
    def Kadane(self,nums):
        current_sum=0
        maxsum=nums[0]
        for num in nums:
            current_sum=max(num,current_sum+num)
            maxsum=max(maxsum,current_sum)
        return maxsum