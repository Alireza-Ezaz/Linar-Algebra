import numpy as np


def echelon_form_recursive(matrix):
    # Using recursive Algorithem

    matrix = np.array(matrix)
    row, column = matrix.shape
    if (row == 0 or column == 0):
        return matrix
    for i in range(len(matrix)):  # len(matrix) is the number of rows actually
        if matrix[i, 0] != 0:
            break
    else:
        sub_Matrix = matrix[:, 1:]  # set aside first column because it is all zeros
        return np.hstack([matrix[:, 0: 1], sub_Matrix])
        # if non-zero element not happen not in the first row,
        # we must interchenge rows(Interchenge)
    if i > 0:
        ith_row = matrix[i].copy()
        matrix[i] = matrix[0]
        matrix[0] = ith_row

    # we should divide first row by first element in it to reach 1(Scaling)
    matrix[0] /= matrix[0, 0]
    matrix[1:] -= matrix[0] * matrix[1:, 0:1]

    # we perform REF on matrix from second row, from second column
    sub_Matrix = echelon_form(matrix[1:, 1:])

    # we add first row and first (zero) column, and return
    return np.vstack([matrix[:1], np.hstack([matrix[1:, :1], sub_Matrix])])


def reduced_Echelon_form(matrix):
    matrix = np.array(matrix)

    leading_position = 0
    rows, columns = matrix.shape
    step_counter = 0
    for r in range(rows):
        if leading_position >= columns:
            break
        ith_row = r

        while matrix[ith_row, leading_position] == 0:
            ith_row += 1
            if ith_row == rows:
                ith_row = r
                leading_position += 1
                if columns - 1 == leading_position:
                    break
        # print(leading_position)
        temp = matrix[ith_row].copy()
        matrix[ith_row] = matrix[r]
        matrix[r] = temp
        # print(r)
        if matrix[r, leading_position] != 0:  # Scaling
            step_counter += 1
            matrix[r] /= matrix[r, leading_position]
            print('Step', step_counter, ': Scaling\n', matrix, '\n')
        for i in range(rows):
            if (i != r):  # Replacement
                step_counter += 1
                matrix[i] -= matrix[i, leading_position] * matrix[r]
                print('Step ', step_counter, ': Row Replacement\n', matrix, '\n')

        leading_position += 1

    return matrix


print('Coefficient Matrix is :\n', coefficient_Matrix)
print(len(coefficient_Matrix))
augmented_Matrix = np.hstack(
    [coefficient_Matrix, np.array(list(map(int, input().split()))).reshape(coefficient_Dim, 1)])
print('Augmented Matrix is:\n', augmented_Matrix, '\n\n')
final_Matrix = reduced_Echelon_form(augmented_Matrix)

flag = True
flag2 = True

for i in range(len(final_Matrix)):
    if np.all(final_Matrix[i] == 0):
        flag2 = False

    elif list(final_Matrix[i, 0:len(final_Matrix)]) == [0] * len(final_Matrix) and final_Matrix[i, len(final_Matrix)]:
        print('\n\nThere is No Answer!!!!!!!!!!')
        flag = False
        break

if flag and flag2:
    print('The Answer is : ', final_Matrix[:, len(final_Matrix)])
elif flag and not (flag2):
    print('\n\nThere are too many answers!!!!!!!')
