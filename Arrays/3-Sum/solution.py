class Solution:
    def threeSum(nums):
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            needed=-(nums[i])
            left=i+1
            right=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while left<right:
                if needed>(nums[left]+nums[right]):
                    left+=1
                elif needed<(nums[left]+nums[right]):
                    right-=1
                else:
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[left]==nums[right+1]:
                        right-=1
        return ans