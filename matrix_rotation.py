def rotate(matrix):
    rotated_matrix = []
    for number_row in matrix:
        new_row = []
        for bit in range(len(number_row)):
            new_row.insert(0, number_row[bit])
        rotated_matrix.append(new_row)
    return rotated_matrix


def main():
    test_matrix = [[1, 2], [3, 4]]
    expected = [[3, 1], [4, 2]]
    print(rotate(test_matrix))


main()
