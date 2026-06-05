class Solution:
    def isAnagram(self,s,t):
        if len(s)!=len(t):
            return False
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for j in t:
            if j not in d:
                return False
            d[j]-=1
        for k in d:
            if d[k]!=0:
                return False
        return True