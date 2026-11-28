class Solution:
    @staticmethod
    def findsubsets(index,arr,temp,ansList):
        ansList.append(temp.copy())
        for i in range(index,len(arr)):
            if i!= index and arr[i] == arr[i-1]:
                continue
            temp.append(arr[i])
            Solution.findsubsets(i+1,arr,temp,ansList)
            temp.pop()

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ansList=[]
        temp=[]
        Solution.findsubsets(0,nums,temp,ansList)
        return ansList
        