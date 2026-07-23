class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        n = len(s)
        max_length = float('-inf')
        freq={}
        for right in range(n):
            right_char = s[right]
            freq[right_char] = freq.get(right_char,0)+1
            max_freq = max(freq.values())
            window_length = right-left+1
            diff =  window_length -  max_freq 
            while diff  > k:
                left_char = s[left]
                freq[left_char] -=1
                left  +=1
                if(freq[left_char] ==0 ):
                    del freq[left_char]
                max_freq = max(freq.values())
                window_length = right-left+1
                diff =  window_length -  max_freq
            res = right -left+1
            max_length = max(max_length,res)
        return max_length

        