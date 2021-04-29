# Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A. The
# sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the
# third element is invalid. Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Find
# and return the required subarray. NOTE: If there is a tie, then compare with segment's length and return segment
# which has maximum length. If there is still a tie, then return the segment with minimum starting index.
#


def maxset(A):
    max_sum = 0
    max_start = 0
    max_end = 0
    max_end = 0
    sum1 = 0
    start = 0
    end = 0
    for i in range(0, len(A)):
        if A[i] < 0:
            if sum1 >= max_sum:
                max_sum = sum1
                max_start = start
                max_end = end
            sum1 = 0
            start = i + 1
            end = i + 1
        else:
            sum1 += A[i]
            end += 1
    if max_sum >= sum1:
        return A[max_start:max_end]
    else:
        return A[start:end]


# def maxset(A):
#     i = 0;
#     maxi = -1;
#     index = 0;
#     a = []
#
#     while i < len(A):
#         while i < len(A) and A[i] < 0:
#             i += 1
#         l = []
#         index = i
#         while i < len(A) and A[i] >= 0:
#             l.append(A[i])
#             i += 1
#         if (sum(l) > maxi):
#             a = l
#             maxi = sum(l)
#
#     return a


if __name__ == "__main__":
    # ans = maxset([0, 0, -1, 0])
    # ans = maxset([10, -1, 2, 3, -4, 100])
    ans = maxset([1, 2, 3, -7, 2, 3])
    print(ans)


# Input 1:
#  A = [1, 2, 5, -7, 2, 3]
# Input 2:
#  A = [10, -1, 2, 3, -4, 100]
#
# Example Output
# Output 1:
#  [1, 2, 5]
# Output 2:
#  [100]
#
#
#
# Example Explanation
# Explanation 1:
#  The two sub-arrays are [1, 2, 5] [2, 3].
#  The answer is [1, 2, 5] as its sum is larger than [2, 3].
#
# Explanation 2:
#  The three sub-arrays are [10], [2, 3], [100].
#  The answer is [100] as its sum is larger than the other two.
