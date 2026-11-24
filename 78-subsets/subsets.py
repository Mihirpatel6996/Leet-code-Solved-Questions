class Solution:
    @staticmethod
    def solve(ip:list[int],op:list[int],ans:list[int]):
        if len(ip) == 0:
            ans.append(op)
            return
        
        op1 = op
        op2 = op + [ip[0]]
        remaining = ip[1:]
        Solution.solve(remaining,op1,ans)
        Solution.solve(remaining,op2,ans)
        return

    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        Solution.solve(nums,[],ans)

        return ans


        
        