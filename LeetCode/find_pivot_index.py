# https://leetcode.com/problems/find-pivot-index/
# Problem No: 724
# Time Complexity: O(N)

class Solution:

    # solution with O(N) space complexity
    def find_pivot_index(self, nums):
        length_of_nums = len(nums)

        # since we doing a prefix sum we will start from the end and insert will be a costly op, hence we initialize
        # with 0
        prefix_sum = [0] * length_of_nums
        p = 0

        # we calc prefix sum from right to left because question demands **leftmost** pivot
        # nums = [-1,-1,0,0,-1,-1]
        # traversing nums from L to R => prefix_sum=[0,-1,-2,-2,-2,-3] and when we traverse this we obtain
        # rightmost pivot
        # traversing nums from R to L => prefix_sum=[-3,-2,-2,-2,-1,0] and in this we get leftmost pivot
        for i in range(length_of_nums - 1, -1, -1):
            prefix_sum[i] = p
            p += nums[i]
        p = 0

        # when there is a match of value we return that index otherwise -1
        for i in range(length_of_nums):
            if prefix_sum[i] == p:
                return i
            p += nums[i]
        else:
            return -1

    # solution with O(1) space complexity
    def findPivot(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        for index, element in enumerate(nums):
            if left_sum == total_sum - left_sum - element:
                return index
            left_sum += element
        else:
            return -1


if __name__ == "__main__":
    sol = Solution()
    # ans = sol.find_pivot_index([-1, -1, 0, 0, -1, -1])  # expected ans 2
    ans = sol.findPivot([1, 7, 3, 6, 5, 6])
    print(ans)

# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11
#
# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
#
# Example 3:
# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0
