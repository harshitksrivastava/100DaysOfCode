# https://leetcode.com/problems/majority-element/
# Problem No: 169
# Time Complexity: O(N)


class Solution:

    # returns the element with maximum occurrences using Boyer-Moore Voting Algo only because question states 
    # majority element always exist otherwise we need to verify the candidate obtained.
    # SC: O(1)
    def find_majority_element(self, nums):

        # assuming the first element has max occurrences and making it's count as 1
        majority_element, count = nums[0], 1
        for index_i in range(1, len(nums)):

            # if the element at index_i in nums is equal to present element in majority_element; +1 to count and if not
            # -1 from count
            if majority_element == nums[index_i]:
                count += 1
            else:
                count -= 1

            # if the count of the majority_element reduces to zero, we update the majority_element to the present 
            # element at index_i and initializing it's count as 1
            if count == 0:
                majority_element = nums[index_i]
                count = 1

        return majority_element


if __name__ == "__main__":
    sol = Solution()
    ans = sol.find_majority_element([0,1,2,1,2])
    print(ans)


# Example 1:
# Input: nums = [3,2,3]
# Output: 3
#
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# NOTE: we can use hashmap/dictionary or sorting but they won't have TC: O(N) and SC: O(1)
