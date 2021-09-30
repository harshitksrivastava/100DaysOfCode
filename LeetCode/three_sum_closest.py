import sys
# https://leetcode.com/problems/3sum-closest/
# Problem No: 16
# Time Complexity: O(N^2) for both solutions


class Solution:

    def three_sum_closest(self, nums, target):
        nums.sort()
        closest_diff = sys.maxsize
        length = len(nums)
        for index in range(length):
            starting_index = index + 1
            ending_index = length - 1
            while starting_index < ending_index:
                curr_sum = nums[index] + nums[starting_index] + nums[ending_index]
                diff = abs(curr_sum - target)
                if curr_sum < target:
                    starting_index += 1
                else:
                    ending_index -= 1

                if diff < abs(closest_diff - target):
                    closest_diff = curr_sum
        return closest_diff

    # this functions uses concept of a+b+c = d  =>  a+b => d-c
    # this has better execution time
    def sum_three_closest(self, nums, target):
        nums.sort()

        # var to store the min diff with desired target
        closest_diff = sys.maxsize
        length = len(nums)
        for index in range(length):

            updated_target = target - nums[index]
            starting_index = index + 1
            ending_index = length - 1

            while starting_index < ending_index:
                curr_sum = nums[starting_index] + nums[ending_index]
                diff = updated_target - curr_sum

                # if we reach a stage where the desired target sum exists as triplets then we don't need to execute
                # further and we can simply return sum/target
                if curr_sum == updated_target:
                    return curr_sum+nums[index]

                # this if else block is for pointer updation
                if curr_sum < updated_target:
                    starting_index += 1
                else:
                    ending_index -= 1

                # to check if the diff of present triplets' sum and target is minimum and updating for same.
                if abs(diff) < abs(target-closest_diff):
                    closest_diff = curr_sum+nums[index]

        return closest_diff


if __name__ == "__main__":
    sol = Solution()
    ans = sol.sum_three_closest([-1, 2, 1, -4], 2)
    print(ans)


# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0

