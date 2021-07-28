# Write a function to find the longest common prefix string amongst an array of strings.\
# If there is no common prefix, return an empty string "".


class Solution:

    def longest_common_prefix(self, strs):
        max_len = len(strs[0])  # the below can be written as len(min(strs,key=len))
        for i in strs:
            max_len = min(max_len, len(i))
        i = 0
        q = -1
        while i < max_len:
            for j in range(0, len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    q = 1
                    break
            if q == 1:
                break
            i += 1
        return strs[0][:i]

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
