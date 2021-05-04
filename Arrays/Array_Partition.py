class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        total_sum = sum(B)
        if total_sum % 3 == 0:
            cum_suffix_sum = [0] * A
            sum1 = total_sum // 3
            ss = 0
            for i in range(A - 1, -1, -1):
                ss += B[i]
                if ss == sum1:
                    cum_suffix_sum[i] = 1
            for i in range(A - 2, -1, -1):
                cum_suffix_sum[i] += cum_suffix_sum[i + 1]
            ss = 0
            ways = 0
            for i in range(0, A - 2):
                ss += B[i]
                if ss == sum1:
                    ways += cum_suffix_sum[i + 2]
            return ways
        return 0


if __name__== '__main__':
    partition = Solution()
    p = partition.solve(5,[1,2,3,0,3])
    print(p)