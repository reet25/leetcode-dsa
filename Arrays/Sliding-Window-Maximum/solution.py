class Solution:
    def slidingWindowMaximum(nums,k):
        from collections import deque
        left=0
        q=deque()
        ans=[]
        for right in range(len(nums)):
            while q and q[0]<left:
                q.popleft()
            while q and nums[q[-1]]<nums[right]:
                q.pop()
            q.append(right)
            if right-left+1<k:
                ans.append(nums[q[0]])
                left+=1
        return ans