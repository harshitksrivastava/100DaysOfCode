# https://leetcode.com/problems/container-with-most-water/
# Problem No: 11
# Time Complexity: O(n) Greedy Approach

class Solution:

    # function returns the maximum area formed by two entries of given list along with x-axis
    def maxArea(self, height):
        # i-> starting point , j->ending point of height
        max_area, i, j = 0, 0, len(height) - 1
        while i < j:
            # as the container needs to be closed so the minimum will be chosen otherwise the water may spill out
            h = min(height[i], height[j])

            # calculating the horizontal distance between the two points from heights
            width = j - i
            max_area = max(max_area, h * width)

            # we move both pointers if both have same value, or move the pointer from where height is smaller i.e
            # if height at start is smaller then move i forward otherwise j will be moved
            if height[i] == height[j]:
                i += 1
                j -= 1
            elif height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

    # this is a bit faster than the above approach
    def max_area_with_for_loop(self, height):
        max_area, i, j = 0, 0, len(height) - 1
        for k in range(len(height) - 1, -1, -1):
            if height[i] < height[j]:
                max_area, i = max(max_area, min(height[i], height[j]) * k), i + 1
            else:
                max_area, j = max(max_area, min(height[i], height[j]) * k), j - 1
        return max_area


if __name__ == "__main__":
    sol = Solution()
    ans = sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(ans)

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.
#
# Example 2:
# Input: height = [1,1]
# Output: 1
#
# Example 3:
# Input: height = [4,3,2,1,4]
# Output: 16
#
# Example 4:
# Input: height = [1,2,1]
# Output: 2
