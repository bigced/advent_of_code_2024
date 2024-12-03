from advent_of_code_2024.day_1.day_1 import calculate_total_distance, parse_data, calculate_total_distance_part2


def test_get_total_distance():
    data = """3   4
4   3
2   5
1   3
3   9
3   3"""
    total_distance = calculate_total_distance(data)
    assert 11 == total_distance


def test_parse_data():
    data = """3   4
4   3
2   5
1   3
3   9
3   3"""

    left_list, right_list = parse_data(data)
    assert left_list == [3, 4, 2, 1, 3, 3]
    assert right_list == [4, 3, 5, 3, 9, 3]


def test_get_total_distance_part2():
    data = """3   4
4   3
2   5
1   3
3   9
3   3"""
    total_distance = calculate_total_distance_part2(data)
    assert 31 == total_distance