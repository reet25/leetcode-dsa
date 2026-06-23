class Solution:
    def minWindowSubstring(s,t):
        need={}
        for i in t:
            if i in need:
                need[i]+=1
            else:
                need[i]=1
        window={}
        required=len(need)
        formed=0
        best_len=float('inf')
        best_left=0
        best_right=0
        left=0
        for right in range(len(s)):
            if s[right] in window:
                window[s[right]]+=1
            else:
                window[s[right]]=1
            if s[right] in need and window[s[right]]==need[s[right]]:
                formed+=1
            while formed==required:
                if right-left+1<best_len:
                    best_len=right-left+1
                    best_left=left
                    best_right=right
                window[s[left]]-=1
                if s[left] in need and window[s[left]]<need[s[left]]:
                    formed-=1
                left+=1
        if best_len==float('inf'):
            return ""
        else:
            return s[best_left:best_right+1]