class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
            li = []
            while A!=0:
                res = A%26
                if res == 0:
                    li.append(chr(90))
                    A = (A//26)-1
                else:
                    li.append(chr(res+64))
                    A = A//26
            print("".join(li[::-1]))


if __name__ == '__main__':
    convert_to_title = Solution()
    convert_to_title.convertToTitle(26)
