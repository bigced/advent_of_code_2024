from advent_of_code_2024.common import get_data_from_file


def parse_data(data):
    left_list = []
    right_list = []
    for line in data.split("\n"):
        left_number, right_number = line.split("  ")
        left_list.append(int(left_number))
        right_list.append(int(right_number))
    return left_list, right_list


def calculate_total_distance(data):
    left_list, right_list = parse_data(data)

    left_list.sort()
    right_list.sort()

    distance = 0

    for i, item in enumerate(left_list):
        distance += abs(left_list[i] - right_list[i])

    return distance


def calculate_total_distance_part2(data):
    left_list, right_list = parse_data(data)

    right_counter = {}

    for item in right_list:
        if item not in right_counter:
            right_counter[item] = 1
        else:
            right_counter[item] += 1

    distance = 0
    for item in left_list:
        distance += item * right_counter.get(item, 0)
    return distance


def main(filename):
    data = get_data_from_file(filename)
    distance = calculate_total_distance(data)
    print(f"distance is {distance}")


def main2(filename):
    data = get_data_from_file(filename)
    distance = calculate_total_distance_part2(data)
    print(f"distance is {distance}")


if __name__ == "__main__":
    main("day_1.txt")
    main2("day_1.txt")
