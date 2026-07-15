class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos_arr = []
        neg_arr =[]
        #seperate positives and negatives
        for i in range(n):
            if nums[i] >= 0:
                pos_arr.append(nums[i])
            else:
                neg_arr.append(nums[i])
        
        # now handle edge cases 

        if(len(neg_arr) == 0):
            nums[:] = [num**2 for num in nums] 
            return nums
        if(len(pos_arr) == 0):
            nums[:]= [num **2 for num in nums]
            nums.reverse()
            return nums
        
        i =0 
        j =0
        m = len(pos_arr)
        n = len(neg_arr)
        id = 0 
        result = []

        pos_arr[:] = [num**2 for num in pos_arr]
        neg_arr[:] = [num**2 for num in neg_arr]
        neg_arr.reverse()
        while (i<m and j<n):
            if pos_arr[i] < neg_arr[j]:
                result.append(pos_arr[i])
                i+=1
            else :
                result.append(neg_arr[j])
                j+=1
        
        while(i<m):
            result.append(pos_arr[i])
            i+=1
        
        while(j<n):
            result.append(neg_arr[j])
            j+=1
        
        return result


        