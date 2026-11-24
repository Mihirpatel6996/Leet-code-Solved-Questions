class Solution:
    @staticmethod
    def solve(ip,op, ans):
        if len(ip) == 0:
            ans.append(op)
            return
        
        if ip[0].isalpha() :
            op1 = op + ip[0].lower()
            op2 = op +ip[0].upper()

            remaining = ip[1:]

            Solution.solve(remaining, op1,ans)
            Solution.solve(remaining,op2,ans)

        else:
            op1 = op +ip[0]
            remaining = ip[1:]
            Solution.solve(remaining,op1,ans)

    def letterCasePermutation(self, s: str) -> list[str]:
        ans=[]
        Solution.solve(s,"",ans)
        return ans
        