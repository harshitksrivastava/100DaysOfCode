class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        I = ""
        if A==0:
            return 0
        while A != 0:
            rem = A % 2
            I = str(rem)+I
            A = A // 2
        return (I)


if __name__ == "__main__":
    binary = Solution()
    ans = binary.findDigitsInBinary(0)
    print(ans)
