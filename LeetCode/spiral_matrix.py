# https://leetcode.com/problems/spiral-matrix/
# Problem No: 54
# Time Complexity: O(M*N)
# Space complexity: O(1). This is because we don't use other data structures.
# Remember that we don't include the output array in the space complexity.


class Solution:
    def spiralOrder(self, matrix):
        top, left = 0, 0
        bottom, right = len(matrix), len(matrix[0])
        output = []
        method = output.append
        while top < bottom and left < right:

            # move right on top most row
            for i in range(left, right):
                method(matrix[top][i])
            top += 1

            # move down on right most column
            for j in range(top, bottom):
                method(matrix[j][right - 1])
            right -= 1

            # check if there is an overlap
            if top < bottom and left < right:

                # move left on bottom most row
                for i in range(right - 1, left - 1, -1):
                    method(matrix[bottom - 1][i])
                bottom -= 1

                # move top on left most column
                for j in range(bottom - 1, top - 1, -1):
                    method(matrix[j][left])
                left += 1

        return output


if __name__ == "__main__":
    sol = Solution()
    ans = sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(ans)


# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
