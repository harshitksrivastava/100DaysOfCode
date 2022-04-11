# https://leetcode.com/problems/implement-strstr/
# Problem No: 28
# Time Complexity:


class Solution:

    def str_str(self, haystack, needle):

        if len(needle) == 0:
            return 0
        elif len(needle) <= len(haystack):
            length_of_needle = len(needle)
            for i in range(len(haystack) - length_of_needle + 1):
                if haystack[i:i + length_of_needle] == needle:
                    return i

        return -1

    def strStr(self,haystack, needle):

        def match(i, haystack1, needle1):
            for j in range(i, i+len(needle1)):
                if needle1[j-i] == haystack1[j]:
                    continue
                else:
                    return False
            return True

        if len(needle) == 0:
            return 0
        length_of_needle = len(needle)
        for i in range(len(haystack) - length_of_needle + 1):
            if haystack[i] == needle[0] and match(i, haystack,needle):
                return i
        return -1

    def str_str_3(self, haystack, needle):
        if len(needle) == 0:
            return 0
        length_of_needle = len(needle)
        for i in range(len(haystack) - length_of_needle + 1):
            if haystack[i] == needle[0]:
                for j in range(i, i + len(needle)):
                    if needle[j - i] == haystack[j]:
                        continue
                    else:
                        break
                else:
                    return i
        return -1