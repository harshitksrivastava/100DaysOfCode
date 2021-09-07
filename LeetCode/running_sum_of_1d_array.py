# https://leetcode.com/problems/running-sum-of-1d-array/
# Problem No: 1480
# Time Complexity: O(n)

import itertools


class Solution:
    def runningSum(self, nums):
        # method 1
        # for i in range(1,len(nums)):
        #     nums[i] +=nums[i-1]
        # return nums

        # method 2 for Python 3.6
        return list(itertools.accumulate(nums))
        # method 3 for Python 3.8 and it is faster than above
        # return itertools.accumulate(nums)


if __name__ == "__main__":
    sol = Solution()
    num = [1, 2, 3, 4]
    ans = sol.runningSum(num)
    target = [1, 3, 6, 10]

    assert ans == target, 'wrong answer'
    print(f"{num} after transformation is {target}.")

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
#
# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
#
# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
