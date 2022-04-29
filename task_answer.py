def task_1(input_points: list) -> int:
    start = input_points[0]
    max_depth = 0
    peak = 0

    for i in input_points[1:]:
        if i > start:
            start = i
            peak = i
        elif i < start and (peak - i) > max_depth:
            max_depth = peak - i
    return max_depth


assert task_1([1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 8, 8, 2]) == 6
