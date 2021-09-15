# https://leetcode.com/problems/product-of-array-except-self/
# Problem No: 238
# Time Complexity:(n)


class Solution:
    def productExceptSelf(self, nums):
        p, product_array = 1, []

        # calculates the left product
        for i in range(len(nums)):
            product_array.append(p)
            p = p * nums[i]
        p = 1

        # calculates the right product
        for i in range(len(nums) - 1, -1, -1):
            product_array[i] *= p
            p *= nums[i]
        return product_array

    def product_except_self_one_pass(self, nums):
        product_array = [1] * len(nums)
        left, right = 1, 1
        for i in range(len(nums)):
            product_array[i] *= left
            product_array[-1 - i] *= right
            left *= nums[i]
            right *= nums[-1 - i]
        return product_array


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    ans = sol.productExceptSelf(nums)
    assert ans == [24, 12, 8, 6], "Incorrect output"
    print(f"{nums} results in {ans} after product except self")


# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
#
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
