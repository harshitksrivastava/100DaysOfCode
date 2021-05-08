# Determine whether an integer is a palindrome. Do this without extra space.
# A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
# ******* NOTE: Negative numbers are not palindromic. *******

# Example :
# Input : 12121
# Output : True/1
#
# Input : 123
# Output : False/0

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        rem = 0
        rev = 0
        if A == 0:
            return 1
        elif A > 0:
            S = A
            while A != 0:
                rem = A % 10
                rev = rev*10+rem
                A = A // 10
            if S == rev:
                return 1
        return 0


if __name__ == "__main__":
    palindome = Solution()
    ans = palindome.isPalindrome(2147447412)
    print(ans)
