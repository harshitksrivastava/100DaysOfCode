# Count pairs with given sum
# Given an array of N integers, and an integer K, find the number of pairs of elements in
# the array whose sum is equal to K.

# it uses hash technique of Dictionary to give optimum result in O(N) time complexity
def get_pairs_count(arr, n, k):
    # code here
    if n <= 1:
        return 0
    dictionary_list = {}
    count = 0
    for i in arr:
        if i not in dictionary_list:
            dictionary_list[i] = 1
        else:
            dictionary_list[i] += 1
    else:
        for i in arr:
            sum1 = k - i
            dictionary_list[i] -= 1
            if sum1 > 0:
                if dictionary_list.get(sum1):
                    count += dictionary_list.get(sum1)

    return count


if __name__ == "__main__":
    N, K = list(map(int, input().split()))
    input_list = list(map(int, input().split()))
    # abc = get_pairs_count([1, 1, 1, 1], 4, 6)
    abc = get_pairs_count(input_list, N, K)
    print(abc)

# Input 1:
# N = 4, K = 6
# arr[] = {1, 5, 7, 1}
# Output: 2
# Explanation:
# arr[0] + arr[1] = 1 + 5 = 6
# and arr[1] + arr[3] = 5 + 1 = 6.
#
# Input 2:
# N = 4, X = 2
# arr[] = {1, 1, 1, 1}
# Output: 6
# Explanation:
# Each 1 will produce sum 2 with any 1.
#
# Input 3:
# N = 49 k = 50 arr = 48 24 99 51 33 39 29 83 74 72 22 46 40 51 67 37 78 76 26 28 76 25 10 65 64 47 34 88 26
# 49 86 73 73 36 75 5 26 4 39 99 27 12 97 67 63 15 3 92 90
# Output: 7  (24,26) (22,28) (46,4) (40,10) (47,3)
