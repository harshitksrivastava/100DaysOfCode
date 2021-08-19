class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        if s[0] == '-' or s[0] == '+' or s[0].isdigit():
            num_dict = {str(i): i for i in range(10)}
            start = 0 if s[0].isdigit() else 1
            try:
                su = 0
                for i in range(start, len(s)):
                    su = su * 10 + num_dict[s[i]]
            finally:
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
