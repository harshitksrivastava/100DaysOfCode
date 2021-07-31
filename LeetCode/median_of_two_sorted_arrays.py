import sys
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).



class Solution:
    """Finds median of an array using binary search approach in O(log(m+n))"""
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # nums1 length should be smaller for this approach to work
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        else:
            lower = 0
            upper = len(nums1)
            n = len(nums1)
            m = len(nums2)
            while lower <= upper:
                part_nums1 = (upper + lower) // 2
                part_nums2 = ((n + m + 1) // 2) - part_nums1
                max1 = nums1[part_nums1 - 1] if part_nums1 > 0 else -sys.maxsize - 1
                max2 = nums2[part_nums2 - 1] if part_nums2 > 0 else -sys.maxsize - 1
                min1 = nums1[part_nums1] if part_nums1 < n else sys.maxsize
                min2 = nums2[part_nums2] if part_nums2 < m else sys.maxsize
                if min2 >= max1 and min1 >= max2:
                    if (n + m) % 2 == 0:
                        return float((max(max1, max2) + min(min1, min2)) / 2)
                    else:
                        return float(max(max1, max2))
                elif max2 > min1:
                    lower = part_nums1 + 1
                else:
                    upper = part_nums1 - 1


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    ans = sol.findMedianSortedArrays(nums1, nums2)
    print(ans)
#
# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
# Example 3:
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
#
# Example 4:
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
#
# Example 5:
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
