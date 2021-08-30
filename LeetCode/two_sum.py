# https://leetcode.com/problems/two-sum/

# Time Complexity: O(n)

class Solution:

    # function returns list of indexes of numbers which add upto given target
    def find_two_sum(self, nums, target):
        # to store number with their index
        nums_dict = {}

        # looping through the nums list
        for i in range(0, len(nums)):

            # j stores the difference of the target and present number from nums
            j = target - nums[i]

            # if j exist in keys of the dictionary/map then we have a match pair
            if j in nums_dict.keys():
                return nums_dict[j], i

            # if j not in dictionary then add the number with it's index
            nums_dict[nums[i]] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    expected = [0, 1]
    target = 9
    sol = Solution()
    ans = sol.find_two_sum(nums, target)
    print(ans)
    assert (nums[ans[0]] + nums[ans[1]]) == target, 'not found'
    print(f"{nums[ans[0]]} and {nums[ans[1]]} at {ans[0]} and {ans[1]} adds up to {target}.")

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
