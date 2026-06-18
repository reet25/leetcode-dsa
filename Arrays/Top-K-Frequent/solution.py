class Solution:
    def topKFrequent(nums,k):
        d={}
        for i in d:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        bucket=[[] for _ in range(len(nums)-1)]
        for num,freq in d.items():
            bucket[freq].append(num)
        ans=[]
        for i in range(len(bucket)-1,-1,-1):
            for j in bucket[i]:
                ans.append(j)
            if len(ans)==k:
                return ans