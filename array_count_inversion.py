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
            inv_count += (mid - i) + 1
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
    input_array = [8, 4, 2, 1]
    count = count_inversion(input_array)
    print(input_array)
    print(count)
