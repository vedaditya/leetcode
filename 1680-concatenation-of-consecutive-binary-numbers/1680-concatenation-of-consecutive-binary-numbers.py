class Solution:
    def concatenatedBinary(self, n: int) -> int:
        def soln(n):
            if n==1:
                return "1"
            else:
                return soln(n-1)+bin(n)[2:]
        return int(soln(n),2)%1000000007