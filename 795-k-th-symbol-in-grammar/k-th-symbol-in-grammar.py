class Solution:
    @staticmethod
    def solve(n:int,k:int)->int:
        if n==1 and k==1:
            return 0
        mid = pow(2,n-1)//2

        if (k <= mid ):
            return Solution.solve(n-1, k)
        else:
            return 1-Solution.solve(n-1, k-mid)
    def kthGrammar(self, n: int, k: int) -> int:
        ele = Solution.solve(n,k)
        return ele

        