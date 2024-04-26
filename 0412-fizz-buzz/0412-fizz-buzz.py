class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a=[]
        for i in range(1,n+1):
            na=""
            t= i%3==0
            f= i%5==0
            ft=i%15==0
            if ft:
                na+="FizzBuzz"
            elif t:
                na+="Fizz"
            elif f:
                na+="Buzz"
            else:
                na+=f'{i}'
            a.append(na)
        return a