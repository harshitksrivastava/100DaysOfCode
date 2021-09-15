# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of
# numbers. If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e.,
# sorted in ascending order). The replacement must be in place and use only constant extra memory.

def next_permutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums) - 1, 0, -1):
        if nums[i - 1] < nums[i]:
            temp = nums[i:]
            temp.sort()
            j = 0
            while j < len(temp):
                if temp[j] > nums[i - 1]:
                    temp[j], nums[i - 1] = nums[i - 1], temp[j]
                    nums[i:] = temp
                    f = 1
                    break
                else:
                    j += 1
            if f == 1:
                return nums
    else:
        nums.sort()
        return nums


if __name__ == "__main__":
    # input_array = [4, 5, 7, 3, 2, 5, 4, 2, 1]
    input_array = [1]
    a = next_permutation(input_array)
    print(a)

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Input: nums = [3,2,1]
# Output: [1,2,3]
# Input: nums = [1]
# Output: [1]
# Input: nums = [1,1,5]
# Output: [1,5,1]
