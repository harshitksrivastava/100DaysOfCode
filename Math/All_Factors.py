import math


class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        factors = []
        lower_limit = math.sqrt(A)
        for i in range(1, int(lower_limit) + 1):
            if A % i == 0:
                factors.append(i)
                if i != lower_limit:
                    factors.append(A // i)
        return sorted(factors)


if __name__ == '__main__':
    allfacto = Solution()
    # 38808
    li = allfacto.allFactors(36)
    print(li)
