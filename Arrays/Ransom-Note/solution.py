class Solution:
    def canConstruct(self,ransomNote,magazine):
        d={}
        for i in magazine:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in ransomNote:
            if i not in d or d[i]==0:
                return False
            d[i]+=1
        return True