# https://leetcode.com/problems/climbing-stairs/
# Problem No: 70
# Time Complexity: o(n)

class Solution:

    # bottom up approach with O(1) constant space
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        for i in range(n - 2, -1, -1):
            one, two = one + two, one
        return one

    # bottom up approach with o(n) space approach
    def climb_stairs_with_dynamic_array(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[n] = 1
        dp[n - 1] = 1
        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]


if __name__ == "__main__":
    sol = Solution()
    ans = sol.climbStairs(5)
    assert ans == 8, "incorrect answer"
    print("Correct answer")

