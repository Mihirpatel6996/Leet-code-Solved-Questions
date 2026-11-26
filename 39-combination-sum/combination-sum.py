class Solution:
    @staticmethod
    def findCombinations(index, arr, target,ans,op):
        if index == len(arr):
            if target == 0:
                ans.append(op.copy())
            return
        
        if arr[index] <= target:
            op.append(arr[index])
            Solution.findCombinations(index,arr,target-arr[index],ans,op)
            op.pop()
        
        Solution.findCombinations(index+1, arr,target,ans,op)

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        op = []

        Solution.findCombinations(0,candidates,target, ans,op)
        return ans

        