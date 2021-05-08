class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        # a = str(abs(A))
        # a = int(a[::-1])
        # if A < 0:
        #     a = -a
        # if a > 2147483647 or a < -2147483647:
        #     return 0
        # return a
        max1 = (2 ** 31)
        print(max1)
        rev = 0
        flag = 1
        a = A
        if A < 0:
            flag = -1
            A = A * flag
        while A != 0:
            rem = A % 10
            rev = rev * 10 + rem
            A = A // 10
        if a < 0:
            rev * flag
        if rev > max1 - 1 or rev < max1 * (-1):
            return 0
        return rev


if __name__ == '__main__':
    rev1 = Solution()
    ans = rev1.reverse(-1146467285)
    print(ans)
