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


def insert(intervals, new_interval):
    intervals.insert(len(intervals) - 1, new_interval)
    intervals.sort(key=lambda i: i.start)
    len_intervals = len(intervals)
    pre = 0
    for i in range(1, len_intervals):
        if intervals[pre].end >= intervals[i].start:
            intervals[pre].end = max(intervals[pre].end, intervals[i].end)

        else:
            pre += 1
            intervals[pre] = intervals[i]

    return intervals[:pre + 1]

if __name__ == "__main__":
    # input_array = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # input_array = [(6037774, 6198243), (6726550, 7004541), (8842554, 10866536), (11027721, 11341296),
    #                (11972532, 14746848), (16374805, 16706396), (17557262, 20518214), (22139780, 22379559),
    #                (27212352, 28404611), (28921768, 29621583), (29823256, 32060921), (33950165, 36418956),
    #                (37225039, 37785557), (40087908, 41184444), (41922814, 45297414), (48142402, 48244133),
    #                (48622983, 50443163), (50898369, 55612831), (57030757, 58120901), (59772759, 59943999),
    #                (61141939, 64859907), (65277782, 65296274), (67497842, 68386607), (70414085, 73339545),
    #                (73896106, 75605861), (79672668, 84539434), (84821550, 86558001), (91116470, 92198054),
    #                (96147808, 98979097)]
    # new_interval1 = [36210193, 61984219]
    input_array = list(map(list, input_array))

    # input_array = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]

    new_interval1 = [36210193, 61984219]
    a1 = insert(input_array, new_interval1)
    input_array.append(new_interval1)
    input_array.sort()
    print(input_array)
    arr = merge(input_array)
    print("From Merge", arr)
    print("From insert", a1)

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping
