class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i =0
        j=0
        res = float('-inf')
        k =0
        freq = {}
        n = len(s)
        
        while j < n:
            freq[s[j]] = freq.get(s[j],0)+1

            if len(freq) == j-i+1:
                res = max(res, j-i+1)
            
            while len(freq) < j-i+1 :
                if freq[s[i]] == 1:
                    freq.pop(s[i])
                else:
                    freq[s[i]] -=1
                
                i+=1
            
            j+=1
            
        return 0 if res == float(-inf) else res
            

        