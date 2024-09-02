def merge_intervals(intervals):
    sorted_intervals = sorted(intervals)

    merged = []

    for interval in sorted_intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))

    return merged


if __name__ == "__main__":
    input_intervals = [(25, 30), (2, 19), (14, 23), (4, 8)]
    merged_intervals = merge_intervals(input_intervals)
    print(merged_intervals)
