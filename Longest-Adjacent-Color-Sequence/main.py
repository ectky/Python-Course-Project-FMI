import argparse

matrix_rows = 0
matrix_cols = 0
matrix = []
visited = []


# reset the global values before searching every file
def reset_values():
    global matrix, visited, matrix_rows, matrix_cols
    matrix_rows = 0
    matrix_cols = 0
    matrix = []
    visited = []


def search_area(m_row, m_col, curr_area):
    # append the searched row and col to the visited
    # so they don't get visited again
    visited.append((m_row, m_col))
    curr_area.append((m_row, m_col))
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # recursively search through the matrix with the newly defined
    # row and column which are moved down, right, up or left of the old ones
    for mx, my in moves:
        curr_row, curr_col = m_row + mx, m_col + my
        if 0 <= curr_row < len(matrix) and 0 <= curr_col < len(matrix[curr_row]):
            if matrix[m_row][m_col] == matrix[curr_row][curr_col] \
                    and (not (curr_row, curr_col) in visited):
                search_area(curr_row, curr_col, curr_area)

    return curr_area


def get_longest_adjacent_sequence():
    # check if matrix consists of equal colors and return the product of the dimensions
    if sum([i.count(matrix[0][0]) for i in matrix]) == matrix_rows * matrix_cols:
        return matrix_rows * matrix_cols

    longest_sequence = 0

    # search for sequences in the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if (row, col) not in visited:
                area = search_area(row, col, [])

                if len(area) > longest_sequence:
                    longest_sequence = len(area)

    return longest_sequence


# loading the matrix and the matrix dimensions
# with the data from the file with specified file name
def load_file_data(file_name_arg):
    global matrix_rows, matrix_cols
    with open('tests/' + file_name_arg) as file:
        lines = file.readlines()
        dimensions = lines.pop(0).split(' ')

        matrix_rows = int(dimensions[0])
        matrix_cols = int(dimensions[1])

        for line in lines:
            matrix.append(line.split())


if __name__ == "__main__":
    # registration of input parser
    parser = argparse.ArgumentParser(
        description='A program that finds the longest adjacent sequence of colors in a matrix')
    parser.add_argument('file_names', metavar='N', type=str, nargs='+',
                        help='The name of the test file that the program should run.')
    args = parser.parse_args()

    for file_name in args.file_names:
        reset_values()
        load_file_data(file_name)
        print(get_longest_adjacent_sequence())
