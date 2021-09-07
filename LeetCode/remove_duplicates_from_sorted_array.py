# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Problem No: 26
# Time Complexity: O(n)


class Solution:

    def remove_duplicates(self, nums):
        k = 0
        i = 0
        if len(nums) == len(set(nums)):
            return len(nums)
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
        return k + 1


if __name__ == '__main__':
    sol = Solution()
    ans = sol.remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(ans)


# int k = removeDuplicates(nums); // Calls your implementation
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }