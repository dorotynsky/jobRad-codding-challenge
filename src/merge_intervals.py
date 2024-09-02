def merge_intervals(intervals):
    """
    Merge overlapping intervals.

    :param intervals: List of intervals where each interval is represented as a tuple (start, end)
    :return: List of merged intervals
    """

    # Sort intervals by the first element
    sorted_intervals = sorted(intervals)

    # Create a list to hold merged intervals
    merged = []

    for interval in sorted_intervals:
        # If the merged list is empty or current interval does not overlap with the last merged interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # There is overlap, so we merge the current interval with the previous one
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))

    return merged


# example usage
if __name__ == "__main__":
    input_intervals = [(25, 30), (2, 19), (14, 23), (4, 8)]
    merged_intervals = merge_intervals(input_intervals)
    print(merged_intervals)
