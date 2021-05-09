class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        if A > 1:
            max_limit = int(A ** 0.5)

            for i in range(2, max_limit + 1):
                if A % i == 0:
                    return 0
            else:
                return 1
        else:
            return 0

    def seive(self,A):
        I=[]
        for i in range(0,A+1):
            p = self.isPrime(i)
            if p==1:
                I.append(i)
        return I


if __name__ == "__main__":
    pascal = Solution()
    ans = pascal.seive(18)
    print(ans)