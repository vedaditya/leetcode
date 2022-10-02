class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dic=dict()
        def soln(N,target,K):
            if N==1 and target>0 and target<=K:
                return 1
            elif N==1 and (target <1 or target>K):
                return 0
            elif (target,N) in dic:
                return dic[(target,N)]
            else :
                dic[(target,N)]=0
                for i in range(1,K+1):
                    dic[(target,N)]+=soln(N-1,target-i,K)
                dic[(target,N)]=dic[(target,N)]%1000000007
                return dic[(target,N)]
        return soln(n,target,k)