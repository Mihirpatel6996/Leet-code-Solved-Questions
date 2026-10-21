class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        char_counts = {}
        res = 0 
        k =3
        for i in range (len(s)):
            right_char = s[i]
            char_counts[right_char] = char_counts.get(right_char, 0) + 1

            if i >= k :      
                left_char = s[i-k]
                char_counts[left_char] -= 1
                if char_counts[left_char] == 0:
                    del char_counts[left_char]
                
            if i >= k-1:
                if len(char_counts ) == k :
                    res = res + 1
        
        return res




        