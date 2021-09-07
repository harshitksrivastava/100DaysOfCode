# https://leetcode.com/problems/move-zeroes/
# Problem No: 283
# Time Complexity: O(n)

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach 1
        # i:pointer for places with '0' and j:pointer for non-zero number
        # i = 0
        # j = 0
        # while i < len(nums) and j < len(nums):
        #     if nums[i] == 0 and nums[j] != 0:
        #         nums[i], nums[j] = nums[j], 0
        #         i += 1
        #         j += 1
        #     elif nums[i] == 0 and nums[j] == 0:
        #         j += 1
        #     else:
        #         i += 1
        #         j += 1

        # Approach 2 much faster as compared to above approach but same complexity
        # we find a non-zero number and swap it with the last zero number location pointed by pos
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1


if __name__ == "__main__":
    sol = Solution()
    num = [0, 1, 0, 3, 12]
    target = [1, 3, 12, 0, 0]
    sol.moveZeroes(num)
    assert (num == target), 'not found'
    print(f"after moving {num}.")
