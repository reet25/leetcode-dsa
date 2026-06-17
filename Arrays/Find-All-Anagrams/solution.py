class Solution:
    def findAllAnagrams(s,p):
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d1={}
        ans=[]
        left=0
        for right in range(len(s)):
            if s[right] in d1:
                d1[s[right]]+=1
            else:
                d1[s[right]]=1
            if right-left+1>len(p):
                d1[s[left]]-=1
                if d1[s[left]]==0:
                    del d[s[left]]
            if right-left==len(p):
                if d==d1:
                    ans.append(left)
        return ans