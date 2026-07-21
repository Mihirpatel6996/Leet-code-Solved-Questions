class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
         # code here
        left = 0
        n = len(fruits)
        freq={}
        res = 0
        
        for right in range (n):
            tree = fruits[right]
            freq[tree] = freq.get(tree,0)+1
            
            while (len(freq) > 2):
                left_char = fruits[left]
                freq[left_char] -= 1
                if(freq[left_char] == 0):
                    del freq[left_char]
                left +=1
        
            res = max(res, right-left+1)
        return res

        