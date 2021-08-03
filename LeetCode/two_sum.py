# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


class Solution:
    def find_two_sum(self, nums, target):
        """ function returns list of indexes of numbers which add upto given target"""
        nums_dict = {}          # to store number with their index
        ans_list = []           # to store the final index of the result obtained
        for i in range(0, len(nums)):
            j = target - nums[i]                # j stores the difference of the target and present number from nums
            if j in nums_dict.keys():           # if j exist in keys of the dictionary/map then we have a match pair
                ans_list.extend([nums_dict[j], i])
                break
            else:
                nums_dict[nums[i]] = i          # if j not in dictionary then add the number with it's index
        return ans_list


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
