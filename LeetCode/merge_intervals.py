# https://leetcode.com/problems/merge-intervals/
# Problem No: 56
# Time Complexity: O(n log n)   since we sorting, hence O(n log n) is dominating.
# Space Complexity: O(n)


class Solution:

    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        temp = [intervals[0]]

        # this is a faster method as append is stored and not referenced again and again
        method = temp.append
        for i in range(1, len(intervals)):
            if intervals[i][0] <= temp[-1][1]:
                if intervals[i][1] > temp[-1][1]:
                    temp[-1][1] = intervals[i][1]
            else:
                method(intervals[i])
        return temp


if __name__ == "__main__":
    sol = Solution()
    # ans = sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    ans = sol.merge([[1, 4], [4, 5]])
    print(ans)
