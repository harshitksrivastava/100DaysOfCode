class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        bulb = 0
        i = 0
        while i < len(A):
            bb = 0
            lower_end_point = i - B + 1
            upper_end_point = i + B - 1
            if lower_end_point < 0:
                lower_end_point = 0
            if upper_end_point >= len(A):
                upper_end_point = len(A) - 1
            for j in range(upper_end_point, lower_end_point - 1, -1):
                if A[j] == 1:
                    bb += 1
                    i = j + B
                    break
            if bb == 0:
                return -1
            else:
                bulb += bb
        return bulb


if __name__ == "__main__":
    B1 = [1, 1, 1, 1, 1, 0, 0]
    Am = Solution()
    fact = Am.solve(B1, 3)
    print("factorial is", fact)
