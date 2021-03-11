from sys import argv
import re


def get_longest_adjacent_sequence(matrix):
    longest_sequence = 0
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = []

    def search_area(x, y, curr_area):
        visited.append((x, y))
        curr_area.append((x, y))

        for mx, my in moves:
            curr_x, curr_y = x + mx, y + my
            if 0 <= curr_x < len(matrix) and 0 <= curr_y < len(matrix[curr_x]):
                if matrix[x][y] == matrix[curr_x][curr_y] and (not (curr_x, curr_y) in visited):
                    search_area(curr_x, curr_y, curr_area)
        return curr_area

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if (x, y) not in visited:
                curr_area = search_area(x, y, [])
                if len(curr_area) > longest_sequence:
                    longest_sequence = len(curr_area)

    return longest_sequence


def load_file_data(file_name):
    with open(file_name) as f:
        lines = f.readlines()

    w_and_h = re.split('[ \n]', lines[0])
    result = [['' for x in range(int(w_and_h[0]))] for y in range(int(w_and_h[1]))]

    l, i = 0, 0
    for line in lines[1:]:
        for char in line:
            if char != "\n" and char != " ":
                result[l][i] = char
                i += 1
        l += 1
        i = 0

    return result


if __name__ == "__main__":
    for file in argv[1:]:
        data = load_file_data(file)
        print(get_longest_adjacent_sequence(data))
