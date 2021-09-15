# https://leetcode.com/problems/subarray-sum-equals-k/
# Problem No: 560
# Time Complexity and Space Complexity: O(n)


class Solution:
    def subarraySum(self, nums, k):

        # 0 as sum-k = 0 edge case
        prefix_map = {0: 1}
        count = 0
        curr_sum = 0
        for i in nums:
            curr_sum += i
            diff = curr_sum - k
            count += prefix_map.get(diff, 0)
            prefix_map[curr_sum] = 1 + prefix_map.get(curr_sum, 0)
        return count


if __name__ == "__main__":
    sol = Solution()
    ans = sol.subarraySum([1, -1, 1, 1, 1, 1],3)
    print(ans)


# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
#
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
