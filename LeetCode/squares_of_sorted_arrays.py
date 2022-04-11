# https://leetcode.com/problems/squares-of-a-sorted-array/
# Problem No: 977
# Time Complexity: O(N)


class Solution:

    def squares_of_sorted_array(self, nums):

        # left_index: starting pointer of nums; right_index: end pointer of nums
        left_index, right_index = 0, len(nums) - 1

        # to store the desired output
        square_sorted_array = []

        # this step reduces the actual time of execution of program
        method = square_sorted_array.append

        # basic idea is to find the bigger absolute value from either ends pointed by left_index and right_index
        # and then append the square of it in the o/p array.
        while left_index <= right_index:
            if abs(nums[left_index]) > abs(nums[right_index]):
                method(nums[left_index] * nums[left_index])
                left_index += 1
            else:
                method(nums[right_index] * nums[right_index])
                right_index -= 1
        # the o/p array will be in desc order, hence we return the reverse of it
        return square_sorted_array[::-1]

    # same as above but the difference is we don't send the reverse of the array obtained
    def sortedSquares(self, nums):
        left = 0
        right = len(nums) - 1
        k = len(nums) - 1
        sortedarray = [0] * len(nums)
        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                sortedarray[k] = nums[right] * nums[right]
                right -= 1
            else:
                sortedarray[k] = nums[left] * nums[left]
                left += 1
            k -= 1
        return sortedarray


if __name__ == "__main__":
    sol = Solution()
    ans = sol.squares_of_sorted_array([-4, -1, 0, 3, 10])
    print(ans)


# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#
# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
