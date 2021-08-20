# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        # removing spaces from starting and ending
        s = s.strip()

        # If the given string is empty
        if len(s) == 0:
            return 0

        # If the starting point is '-' ,'+' or any number b/w 0-9
        if s[0] == '-' or s[0] == '+' or s[0].isdigit():

            # dictionary to hold '0':0 type values
            num_dict = {str(i): i for i in range(10)}

            # determines if we have a digit or a symbol at starting index
            start = 0 if s[0].isdigit() else 1

            # If we encounter a non-digit number then it will not be found in num_dict and an exception will occur the
            # value till point in su will be taken forward in finally block
            try:
                su = 0
                for i in range(start, len(s)):
                    su = su * 10 + num_dict[s[i]]
            finally:
                # the o/p should be in range [-2**31,2**31 -1]
                pos_limit = 2 ** 31
                neg_limit = (-1) * pos_limit
                if s[0] == '-':
                    su = neg_limit if -su < neg_limit else -su
                else:
                    su = pos_limit-1 if su >= pos_limit else su
                return su
        return 0


if __name__ == "__main__":
    sol = Solution()
    ans = sol.myAtoi(" ")
    print(ans)
