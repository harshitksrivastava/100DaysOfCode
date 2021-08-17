# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            return self.addBinary(b, a)
        carry = 0
        len_a = len(a) - 1
        len_b = len(b) - 1
        final = []
        for i in range(len_b + 1):
            ele_a = int(a[len_a - i])
            ele_b = int(b[len_b - i])
            if carry:
                add = carry + ele_a + ele_b
            else:
                add = ele_a + ele_b
            # final = str(add % 2) + final
            final.append(add % 2)
            carry = add // 2
        for j in range(len_b+1, len_a + 1):
            ele_a = int(a[len_a - j])
            if carry:
                add = carry + ele_a
            else:
                add = ele_a
            # final = str(add % 2)+final
            final.append(add % 2)
            carry = add // 2
        if carry:
            # final = str(carry) + final
            final.append(carry)
        return "".join(map(str, final[::-1]))
        # return final


if __name__ == "__main__":
    sol = Solution()
    ans = sol.addBinary("11", "1")
    print(ans)

# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"
