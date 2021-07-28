# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
# element appears only once. The relative order of the elements should be kept the same.

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