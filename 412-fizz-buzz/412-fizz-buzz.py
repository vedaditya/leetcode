class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[str(i+1) for i in range(n)]
        for i in range(2,n,3):
            ans[i]="Fizz"
        for  i in range(4,n,5):
            if ans[i]=="Fizz":
                ans[i]+="Buzz"
            else:
                ans[i]="Buzz"
        return ans 