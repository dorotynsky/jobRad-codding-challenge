import sys


def use_default_intervals():
    """
    Return a default list of intervals predefined in the script.

    :return: List of tuples representing the intervals
    """
    return [(25, 30), (2, 19), (14, 23), (4, 8)]


def read_intervals_from_input():
    """
    Read intervals from user input.

    Users are prompted to enter intervals in the format 'start,end' and type 'done' to finish input.
    :return: List of tuples representing the intervals
    """
    print("Enter intervals in the format 'start,end' and type 'done' when finished:")
    intervals = []
    while True:
        line = input()
        if line.lower() == 'done':
            break
        intervals.append(tuple(map(int, line.split(','))))
    return intervals


def read_intervals_from_file(file_path):
    """
    Read intervals from a specified file.

    Each line in the file should contain an interval formatted as 'start,end'.
    :param file_path: Path to the file containing intervals
    :return: List of tuples representing the intervals
    """
    try:
        with open(file_path, 'r') as file:
            return [tuple(map(int, line.strip().split(','))) for line in file if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)


def merge_intervals(intervals):
    """
    Merge overlapping intervals

    :param intervals: List of intervals where each interval is represented as a tuple (start, end)
    :return: List of merged intervals
    :raises TypeError: If input is not a list of tuples
    :raises ValueError: If any tuple does not contain exactly two elements
    """

    if not isinstance(intervals, list):
        raise TypeError("Input should be a list of tuples representing intervals.")

    for interval in intervals:
        if not isinstance(interval, tuple) or len(interval) != 2:
            raise ValueError("Each interval should be a tuple of exactly two elements (start, end).")
        if not (isinstance(interval[0], (int, float)) and isinstance(interval[1], (int, float))):
            raise ValueError("Both start and end of each interval should be numbers.")
        if interval[0] > interval[1]:
            raise ValueError("The start of each interval should not be greater than the end.")

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


if __name__ == "__main__":
    print("Select input method: 1 for default input, 2 for direct input from keyboard, 3 for input from a file")
    choice = input("Enter choice (1, 2 or 3): ")
    if choice == "1":
        intervals = use_default_intervals()
    elif choice == "2":
        intervals = read_intervals_from_input()
    elif choice == "3":
        file_path = input("Enter file path: ")
        intervals = read_intervals_from_file(file_path)
    else:
        print("Invalid input, exiting.")
        sys.exit(1)

    if intervals:
        merged_intervals = merge_intervals(intervals)
        print("Initial intervals: ", intervals, "\nMerged Intervals: ", merged_intervals)
    else:
        print("No intervals to process")
