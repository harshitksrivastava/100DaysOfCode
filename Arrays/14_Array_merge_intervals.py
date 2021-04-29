# to merge the intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping
# intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input

def merge(intervals):
    intervals_length = len(intervals)
    if intervals_length == 1:
        return intervals
    intervals.sort()
    interval = intervals[0]
    output_array = [interval]
    for i in range(1, intervals_length):
        interval_current_begin = interval[0]
        interval_current_end = interval[1]
        interval_checking_begin = intervals[i][0]
        interval_checking_end = intervals[i][1]
        if interval_current_end >= interval_checking_begin:
            if interval_current_end < interval_checking_end:
                interval[1] = interval_checking_end
            else:
                interval[1] = interval_current_end
        else:
            output_array.append(intervals[i])
            interval = intervals[i]
    return output_array


if __name__ == "__main__":
    input_array = [[1, 3], [2, 6], [8, 10], [15, 18]]
    arr = merge(input_array)
    print(arr)


# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping
