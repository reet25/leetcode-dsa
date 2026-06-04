class Solution:
    def twoSum(self, nums, target):
        d={}
        for i in range(len(nums)):
            needed=target-nums[i]
            if needed in d:
                return [d[needed],i]
            else:
                d[nums[i]]=i