class Solution:
    @staticmethod
    def recursepermute(index,arr,ans):
        if index == len(arr):
            ans.append(arr.copy())
            return
        
        for i in range(index, len(arr)):
            arr[i],arr[index] = arr[index],arr[i]
            Solution.recursepermute(index+1, arr,ans)
            arr[i],arr[index] = arr[index],arr[i]

    def permute(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        Solution.recursepermute(0,nums,ans)
        return ans
        