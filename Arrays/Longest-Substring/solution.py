class Solution:
    def longestSubstring(s):
        left=0
        right=0
        d={}
        max_len=0
        while right<len(s):
            if s[right] in d:
                d[s[right]]+=1
            else:
                d[s[right]]=1
            while d[s[right]]>1:
                d[s[left]]-=1
                left+=1
            current_len=right-left+1
            max_len=max(current_len,max_len)
            right+=1
        return max_len