# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Problem No: 442
# Time Complexity:


class Solution:

    # this technique uses hashmap/dictionary to to count elements
    def find_all_duplicates_using_dictionary(self, nums):
        map = {}
        for element in nums:
            if element not in map:
                map[element] = 1
            else:
                map[element] += 1

        # we are making a copy of the map as iterating it and modifying it at the same time is not allowed
        # we can then make a list of the keys and return it
        # for k,v in list(map.items()):
        #     if v<2:
        #         del map[k]

        # this is a list comprehension filters value based on provided if cond
        return [key for key, value in map.items() if value > 1]

    # this is in-place negate method
    # the idea is to negate the element at (element - 1) index and when we encounter same element again then we check
    # value at (element-1) if it is -ve then we add it to o/p , as we would have changed it to -ve at first encounter
    def find_all_duplicates_using_negate_method(self, nums):

        # list to store o/p numbers
        num_occ_twice = []
        for element in nums:

            # we use abs(element) as there maybe number which may point to later index
            # suppose we [4,3,2,1] so we encounter 4 first and we apply change for element at index 3, here 1 becomes -1
            #  so when we later reach there then -1-1 will become -2 a non valid index hence we use abs
            index = abs(element) - 1

            # if the element at index is -ve we are seeing it for 2nd time, so add it to o/p
            if nums[index] < 0:
                num_occ_twice.append(abs(element))

            # if value is +ve means encountering for first time, and negating it
            nums[index] *= -1

        return num_occ_twice


if __name__ == "__main__":
    sol = Solution()
    # ans = sol.find_all_duplicates_using_dictionary([4, 3, 2, 7, 8, 2, 3, 1])
    ans = sol.find_all_duplicates_using_negate_method([4, 3, 2, 7, 8, 2, 3, 1])
    print(ans)
