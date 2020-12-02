# to minimise the maximum difference  between heights:


def min_height_difference(arr, n, k):
    arr.sort()

    if arr[n - 1] <= k:
        return arr[n - 1] - arr[0]
    else:

        minimum = arr[0] + k
        maximum = arr[n - 1] - k
        ans = arr[n - 1] - arr[0]
        if maximum < minimum:
            maximum, minimum = minimum, maximum
        for i in range(1, n - 1):
            sub = arr[i] - k
            add = arr[i] + k
            if add > maximum and sub < minimum:
                if add - maximum >= minimum - sub:
                    minimum = sub
                else:
                    maximum = add

        return min(maximum - minimum, ans)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        # length = input().split()
        input_array = [2,6,3,4, 7, 2, 10, 3, 2, 1 ]
    min_value = min_height_difference(input_array, len(input_array), 5)
    print(min_value)

# Time Complexity: (N*logN)
# Input :
# arr[] = {1, 10, 14, 14, 14, 15}
#         k = 6
# Maximum difference is 5