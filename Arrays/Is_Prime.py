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


if __name__ == "__main__":
    pascal = Solution()
    ans = pascal.squareSum(5)
    print(ans)