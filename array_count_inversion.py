# Given an array of integers. Find the Inversion Count in the array.
# For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already
# sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the
# maximum. Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

def merge(array, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2
    inv_count = 0
    for i in range(0, n1):
        L[i] = array[left + i]
    for j in range(0, n2):
        R[j] = array[mid + j + 1]
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
            k += 1
        else:
            array[k] = R[j]
            inv_count += (mid - i-left) + 1
            j += 1
            k += 1
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1
    return inv_count


def merge_sort(array, left, right):
    inv = 0
    if left < right:
        mid = (left + right) // 2
        inv += merge_sort(array, left, mid)
        inv += merge_sort(array, mid + 1, right)
        inv += merge(array, left, mid, right)
    return inv


def count_inversion(array):
    inv_count = merge_sort(array, 0, len(array) - 1)
    return inv_count


if __name__ == "__main__":
    input_array = [1, 20, 6, 4, 5]
    count = count_inversion(input_array)
    print(input_array)
    print(count)


# Input: N = 5, arr[] = {2, 4, 1, 3, 5}
# Output: 3
# Explanation: The sequence 2, 4, 1, 3, 5
# has three inversions (2, 1), (4, 1), (4, 3).
#
# Input: N = 5
# arr[] = {2, 3, 4, 5, 6}
# Output: 0
# Explanation: As the sequence is already
# sorted so there is no inversion count.
