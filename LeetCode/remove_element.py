# https://leetcode.com/problems/remove-element/
# Problem No: 27
# Time Complexity and Space Complexity: O(n)

class Solution:
    def removeElement(self, nums, val):
        pointer_start = 0
        pointer_end = len(nums) - 1
        while pointer_start <= pointer_end:
            if nums[pointer_start] != val:
                pointer_start += 1
                continue
            else:
                while pointer_end > pointer_start:
                    if nums[pointer_end] == val:
                        pointer_end -= 1
                    else:
                        break
            nums[pointer_start] = nums[pointer_end]
            pointer_start += 1
            pointer_end -= 1
        return pointer_start



