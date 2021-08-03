class Solution:
    def romanToInt(self, s: str):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        l = len(s)
        if l < 2:
            return roman.get(s)
        sum1 = roman.get(s[l-1])

        for i in range(l - 2, -1, -1):
            if roman.get(s[i]) >= roman.get(s[i + 1]):
                sum1 += roman.get(s[i])
            else:
                sum1 -= roman.get(s[i])
        return sum1


if __name__ == '__main__':
    sol = Solution()
    a = sol.romanToInt("III")
    print(a)
