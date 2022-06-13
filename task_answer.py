def task_1(input_points: list) -> int:
    start = input_points[0]
    min_point = None
    max_depth = 0
    lake_flag = False

    for counter, i in enumerate(input_points[1:], 1):
        if i > start:
            if lake_flag or counter == len(input_points[1:]):
                if (min(start, i) - min_point) > max_depth:
                    max_depth = min(start, i) - min_point
                min_point = None
            lake_flag = False
            start = i
        elif i <= start:
            if min_point is None or i < min_point:
                min_point = i
            lake_flag = True
            if counter == len(input_points[1:]):
                if (min(start, i) - min_point) > max_depth:
                    max_depth = min(start, i) - min_point
                min_point = None
    return max_depth


assert task_1([1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 8, 8, 2]) == 6

assert task_1([5, 2, 5, 1, 7, 0, 3, 4, 2, 6, 1, 4, 4, 4, 5, 6]) == 6

assert task_1([1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 8, 8, 2])
assert task_1([2, 4, 3, 1, 1, 0, 2, 3, 3, 4, 0, 0, 4, 7, 8, 0, 6, 7, 8, 7])
assert task_1(
    [5, 2, 5, 1, 7, 0, 3, 4, 2, 6, 1, 4, 4, 4, 5, 6, 4, 2, 2, 4, 6, 5])
list_of_heights = [5, 2, 5, 1, 7, 0, 3, 4, 2, 6, 1, 4, 4, 4, 5, 6]
