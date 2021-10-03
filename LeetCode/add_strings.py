# https://leetcode.com/problems/add-strings/
# Problem No: 415
# Time complexity: O(N)

class Solution:

    # solution no 1
    def addStrings(self, num1, num2):
        ans = 0
        if len(num1) < len(num2):
            return self.addStrings(num2, num1)
        i = 1
        len_num1 = len(num1)
        len_num2 = len(num2)
        carry = 0
        ans = []
        while len_num2 - i >-1:
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

    # solution no 2
    def add_strings(self, num1, num2):
        if len(num1) < len(num2):
            return self.add_strings(num2, num1)
        res = []
        carry = 0
        ln1 = len(num1) - 1
        ln2 = len(num2) - 1
        while ln1 >= 0 or carry:
            total = 0
            n1 = int(num1[ln1]) if ln1 >= 0 else 0
            n2 = int(num2[ln2]) if ln2 >= 0 else 0
            total = n1 + n2 + carry
            digit, carry = total % 10, total // 10
            res.append(str(digit))
            ln1 -= 1
            ln2 -= 1
        return " ".join(res[::-1])

    # solution no 3
    # def addStrings(self, num1, num2):
    #   number1 = 0
    #   number2 = 0
    #   for i in num1:
    #     temp = ord(i) - 48
    #     number1 = number1 * 10 + temp
    #   for i in num2:
    #     temp = ord(i) - 48
    #     number2 = number2 * 10 + temp
    #   return str(number1+number2)


if __name__ == "__main__":
    sol = Solution()
    ansd = sol.add_strings("237", "284")
    print(ansd)


# Example 1:
# Input: num1 = "11", num2 = "123"
# Output: "134"
#
# Example 2:
# Input: num1 = "456", num2 = "77"
# Output: "533"
#
# Example 3:
# Input: num1 = "0", num2 = "0"
# Output: "0"
