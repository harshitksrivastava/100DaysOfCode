class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        facto = 1
        for i in range(1, A + 1):
            facto = facto * i
        count = 0
        while facto != 0:
            F = facto % 10
            if F != 0:
                return count
            count += 1
            facto = facto // 10
        return count

    def factorial(self, A):
        if A == 0:
            return 1
        return A * (self.factorial(A - 1))


if __name__ == '__main__':
    trailingzero = Solution()
    ans = trailingzero.trailingZeroes(0)
    print(ans)
