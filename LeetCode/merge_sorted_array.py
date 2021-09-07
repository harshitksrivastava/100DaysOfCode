# https://leetcode.com/problems/merge-sorted-array/
# Problem No: 88
# Time Complexity: O(m+n)


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = n + m - 1
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # this loops is utilized when all elements from num1 is copies to the end and we have elements in num2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

    # def merge(self, nums1, m, nums2, n):
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     if n == 0:
    #         return
    #     if m == 0:
    #         for i in range(n):
    #             nums1[i] = nums2[i]
    #         return
    #
    #     p1, p2, p3 = m - 1, n - 1, m + n - 1
    #     while p3 >= 0:
    #         if p1 >= 0 and p2 >= 0:
    #             if nums1[p1] >= nums2[p2]:
    #                 nums1[p3] = nums1[p1]
    #                 p1 -= 1
    #             else:
    #                 nums1[p3] = nums2[p2]
    #                 p2 -= 1
    #         elif p1 >= 0:
    #             nums1[p3] = nums1[p1]
    #             p1 -= 1
    #         else:
    #             nums1[p3] = nums2[p2]
    #             p2 -= 1
    #         p3 -= 1
    #     return


if __name__ == "__main__":
    sol = Solution()
    # nums1 = [0]
    # nums2 = [6]
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    sol.merge(nums1, m, nums2, n)
    print(nums1)

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
#
# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
#
# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1]. The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only
# there to ensure the merge result can fit in nums1.
