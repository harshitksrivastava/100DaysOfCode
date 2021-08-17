class Solution:
    def addStrings(self, num1, num2):
        ans = 0
        if len(num1) < len(num2):
            return self.addStrings(num2, num1)
        i = 1
        len_num1 = len(num1)
        len_num2 = len(num2)
        carry = 0
        ans = []
        while len_num2 - i>-1:
            element_2 = int(num2[len_num2 - i])
            element_1 = int(num1[len_num1 - i])
            sum1 = element_1 + element_2
            if carry:
                sum1 += carry
            if sum1 > 9:
                carry = 1
            else:
                carry=0
            ans.append(str(sum1 % 10))
            i += 1
        while len_num1 - i>-1:
            element_1 = int(num1[len_num1 - i])
            if carry:
                sum1 = carry+element_1
                if sum1 > 9:
                    carry = 1
                else:
                    carry = 0
                ans.append(str(sum1 % 10))
            else:
                ans.extend(list(reversed(num1[0:(len_num1-i)+1])))
                break
            i += 1
        if carry:
            ans.append(str(carry))
        return "".join(ans[::-1])


if __name__ == "__main__":
    sol = Solution()
    ansd = sol.addStrings("237", "284")
    print(ansd)
