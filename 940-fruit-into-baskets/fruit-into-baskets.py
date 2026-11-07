class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
         # code here
        i =0 
        j=0
        n = len(fruits)
        freq={}
        res = 0
        
        while j < n :
            freq[fruits[j]] = freq.get(fruits[j],0)+1
            
            if len(freq) <= 2:
                res = max(res, j-i+1)

            while (len(freq) > 2):
                if(freq[fruits[i]] == 1):
                    freq.pop(fruits[i])
                else :
                    freq[fruits[i]] -= 1

                i +=1
            j+=1   
        return res

        