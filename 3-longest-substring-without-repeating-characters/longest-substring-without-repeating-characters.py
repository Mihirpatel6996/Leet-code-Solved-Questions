class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left =0
        res = float('-inf')
        k =0
        freq = {}
        n = len(s)
        for right in range(n):
            right_char = s[right]
            freq[right_char] = freq.get(right_char,0)+1
            while (freq[right_char] > 1):
                left_char = s[left]
                freq[left_char] -=1
                if(freq[left_char] == 0):
                    del freq[left_char]
                left +=1
                k = right-left+1
            curr_len = right-left+1
            res = max(res,curr_len)
        return 0 if res == float(-inf) else res
            

        