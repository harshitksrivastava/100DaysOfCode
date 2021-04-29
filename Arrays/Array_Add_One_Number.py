class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        i = 0
        while i < len(A):
            if A[i] > 0:
                break
            else:
                i += 1
        num = 0
        for i in range(i, len(A)):
            num = num * 10 + A[i]
        num += 1
        return list(map(int, list(str(num))))


if __name__ == "__main__":
    A1 = [1, 2, 3]
    Am = Solution()
    fact = Am.plusOne(A1)
    print("factorial is", fact)
