# to find largest sum of contiguous sub array O(N) complexity [kadane's Algorithm)

def sum_contiguous_sub_array(arr):
    max_sum = arr[0]
    max_sum_so_far = arr[0]
    for i in arr[1:]:
        max_sum = max(i, max_sum + i)
        max_sum_so_far = max(max_sum, max_sum_so_far)
    return max_sum_so_far


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        length = input().split()
        array_list = list(map(int, input().split()))
        maximum = sum_contiguous_sub_array(array_list)
        print(maximum)

#
# Input:
# N = 5
# arr[] = {1,2,3,-2,5}
# Output: 9
# Explanation: Max sub array sum is 9
# of elements (1, 2, 3, -2, 5) which is a contiguous sub array.
