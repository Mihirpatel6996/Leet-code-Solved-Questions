class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        sentence = [0]*256
        tofind = [0]*256
        left =0 
        min_length = float('inf')
        start = 0
        count =0 

        for ch in t :
            tofind[ord(ch)] +=1 

        for right in range(n):
            right_word = s[right]
            sentence[ord(right_word)] +=1
            if sentence[ord(right_word)] <= tofind[ord(right_word)] :
                count+=1
            while (count == len(t)):
                window_length = right -left+1
                if (min_length > window_length):
                    min_length = window_length
                    start = left
                sentence[ord(s[left])] -=1
                if(sentence[ord(s[left])] < tofind[ord(s[left])]):
                    count -= 1
                left +=1
        return "" if min_length == float('inf') else s[start: start+min_length]
                



        