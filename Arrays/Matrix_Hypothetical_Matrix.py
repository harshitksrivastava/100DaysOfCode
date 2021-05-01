def countLessThanMid(mid, N, K):

    # To store count of elements
    # less than mid
    count = 0

    # Loop through each row
    for i in range(1, min(N, mid) + 1):
        # Count elements less than
        # mid in the ith row
        count = count + min(mid // i, N)

    if (count >= K):
        return False
    else:
        return True

# Function that returns the Kth
# smallest element in the NxM
# Matrix after sorting in an array
def findKthElement(N, K):

    # Initialize low and high
    low = 1
    high = N * N

    # Perform binary search
    while (low <= high):

        # Find the mid
        mid = low + (high - low) // 2

        # Check if the count of
        # elements is less than mid
        if countLessThanMid(mid, N, K):
            low = mid + 1
        else:
            high = mid - 1

    # Return Kth smallest element
    # of the matrix
    return high + 1


if __name__ == '__main__':
        array_list_one = int(input())
        string = int(input())
        fact = findKthElement(array_list_one, string)
        print(fact)
