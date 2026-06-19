class Solution:
    def subarraySumK(nums,k):
        d={0:1}
        current_sum=0
        count=0
        for i in range(len(nums)):
            current_sum+=nums[i]
            needed=current_sum-k
            if needed in d:
                count+=d[needed]
            if current_sum in d:
                d[current_sum]+=1
            else:
                d[current_sum]=1
        return count