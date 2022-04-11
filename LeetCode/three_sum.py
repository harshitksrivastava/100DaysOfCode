# https://leetcode.com/problems/3sum
# Problem No: 15
# Time Complexity: O(n^2)

class Solution:
    def threeSum(self, nums):
        nums.sort()
        output = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            a = nums[i]

            # a+b+c=0    b+c = -a
            t = -a
            s = i + 1
            e = n - 1
            while s < e:
                if nums[s] + nums[e] == t:
                    output.append([nums[i], nums[s], nums[e]])
                    while s < e and nums[s] == nums[s + 1]:
                        s += 1
                    while s < e and nums[e] == nums[e - 1]:
                        e -= 1
                    s += 1
                    e -= 1
                elif nums[s] + nums[e] > t:
                    e -= 1
                elif nums[s] + nums[e] < t:
                    s += 1

        return output


if __name__ == "__main__":
    sol = Solution()
    ans = sol.threeSum([0, 0, 0])
    print(ans)


# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
# Example 2:
# Input: nums = []
# Output: []
#
# Example 3:
# Input: nums = [0]
# Output: []
