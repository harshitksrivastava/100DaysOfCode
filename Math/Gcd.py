class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if A<B:
            A,B = B,A
        while A%B !=0:
            A,B = B,A%B
        return B


if __name__ == '__main__':
    allfacto = Solution()
    li = allfacto.gcd(1,0)
    print(li)
