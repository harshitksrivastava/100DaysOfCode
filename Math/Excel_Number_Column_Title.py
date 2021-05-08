class Solution:
    # @param A: string
    # @returns an integer
    def titleToNumber(self, A):
        result = 0
        j = 0
        for i in range(len(A)-1, -1, -1):
            result += (26 ** j) * (ord(A[i]) - ord('A') + 1)
            j += 1
        print(result)


if __name__ == '__main__':
    title_number = Solution()
    title_number.titleToNumber("ABA")
