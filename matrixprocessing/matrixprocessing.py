def read_positive_ints(prompt=""):
    """Reads two positive integers from user input.

    Parameters:
    prompt (str): Input message for the user.

    Returns:
    tuple: Two positive integers (n, m).
    """
    while True:
        try:
            values = input(prompt).split()

            if len(values) != 2:
                print("You need to enter 2 numbers")
                continue

            n, m = map(int, values)

            if n <= 0 or m <= 0:
                print("The dimensions of the matrix must be positive integers")
                continue

            return n, m

        except ValueError:
            print("Invalid input, please try again")

def read_positive_int(prompt=""):
    """Reads one positive integer from user input.

    Parameters:
    prompt (str): Input message for the user.

    Returns:
    int: Positive integer value.
    """
    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                print("You must enter a positive number")
                continue

            return value

        except ValueError:
            print("Invalid input, please try again")

def read_row(m):
    """Reads one row of a matrix with m elements.

    Parameters:
    m (int): Number of elements in the row.

    Returns:
    list: List of float values.
    """
    while True:
        try:
            row = list(map(float, input().split()))

            if len(row) != m:
                print(f"You need to enter {m} numbers")
                continue

            return row

        except ValueError:
            print("Invalid input, please try again")

def read_matrix(n, m):
    """Reads a matrix of size n x m.

    Parameters:
    n (int): Number of rows.
    m (int): Number of columns.

    Returns:
    list: Matrix as a list of lists.
    """
    matrix = []
    for _ in range(n):
        matrix.append(read_row(m))
    return matrix

def add_matrices(A, B, n, m):
    """Adds two matrices element-wise.

    Parameters:
    A (list): First matrix.
    B (list): Second matrix.
    n (int): Number of rows.
    m (int): Number of columns.

    Returns:
    list: Resulting matrix.
    """
    return [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]

def multiply_by_constant(matrix, n, m, k):
    """Multiplies a matrix by a constant.

    Parameters:
    matrix (list): Input matrix.
    n (int): Number of rows.
    m (int): Number of columns.
    k (float): Constant multiplier.

    Returns:
    list: Resulting matrix.
    """
    return [[matrix[i][j] * k for j in range(m)] for i in range(n)]

def multiply_matrices(A, B, n1, m1, n2, m2):
    """Multiplies two matrices.

    Parameters:
    A (list): First matrix.
    B (list): Second matrix.
    n1 (int): Rows in A.
    m1 (int): Columns in A.
    n2 (int): Rows in B.
    m2 (int): Columns in B.

    Returns:
    list: Resulting matrix.
    """
    result = []
    for i in range(n1):
        row = []
        for j in range(m2):
            value = sum(A[i][k] * B[k][j] for k in range(m1))
            row.append(value)
        result.append(row)
    return result

def transpose_main(matrix, n, m):
    """Transposes matrix along main diagonal.

    Parameters:
    matrix (list): Input matrix.
    n (int): Number of rows.
    m (int): Number of columns.

    Returns:
    list: Transposed matrix.
    """
    return [[matrix[i][j] for i in range(n)] for j in range(m)]

def transpose_side(matrix, n, m):
    """Transposes matrix along side diagonal.

    Parameters:
    matrix (list): Input matrix.
    n (int): Number of rows.
    m (int): Number of columns.

    Returns:
    list: Transposed matrix.
    """
    return [[matrix[n - 1 - i][m - 1 - j] for i in range(n)] for j in range(m)]

def transpose_vertical(matrix, n, m):
    """Reflects matrix along vertical axis.

    Parameters:
    matrix (list): Input matrix.
    n (int): Number of rows.
    m (int): Number of columns.

    Returns:
    list: Transformed matrix.
    """
    return [[matrix[i][m - 1 - j] for j in range(m)] for i in range(n)]

def transpose_horizontal(matrix, n, m):
    """Reflects matrix along horizontal axis.

    Parameters:
    matrix (list): Input matrix.
    n (int): Number of rows.
    m (int): Number of columns.

    Returns:
    list: Transformed matrix.
    """
    return [matrix[n - 1 - i] for i in range(n)]

def determinant(matrix):
    """Calculates determinant of a square matrix.

    Parameters:
    matrix (list): Square matrix.

    Returns:
    float: Determinant value.
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for j in range(n):
        minor_matrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(minor_matrix)
    return det

def minor(matrix, i, j):
    """Calculates minor matrix.

    Parameters:
    matrix (list): Input matrix.
    i (int): Row index.
    j (int): Column index.

    Returns:
    list: Minor matrix.
    """
    return [row[:j] + row[j+1:] for k, row in enumerate(matrix) if k != i]

def cofactor_matrix(matrix):
    """Calculates cofactor matrix.

    Parameters:
    matrix (list): Input matrix.

    Returns:
    list: Cofactor matrix.
    """
    n = len(matrix)
    cof_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            sign = (-1) ** (i + j)
            row.append(sign * determinant(minor(matrix, i, j)))
        cof_matrix.append(row)
    return cof_matrix

def inverse_matrix(matrix):
    """Calculates inverse matrix.

    Parameters:
    matrix (list): Square matrix.

    Returns:
    list: Inverse matrix or None.
    """
    det = determinant(matrix)
    if det == 0:
        return None
    cof = cofactor_matrix(matrix)
    n = len(cof)
    adj = [[cof[j][i] for j in range(n)] for i in range(n)]
    return [[adj[i][j] / det for j in range(n)] for i in range(n)]

def print_matrix(matrix):
    """Prints matrix in formatted form.

    Parameters:
    matrix (list): Matrix to print.

    Returns:
    None
    """
    for row in matrix:
        formatted_row = []
        for x in row:
            if isinstance(x, float):
                x = round(x + 1e-8, 2)
                if x.is_integer():
                    x = int(x)
            formatted_row.append(x)
        print(*formatted_row)

def main_menu():
    """Displays menu options.

    Parameters:
    None

    Returns:
    None
    """
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")

def matrix_operations():
    """Runs matrix calculator program.

    Parameters:
    None

    Returns:
    None
    """
    while True:
        main_menu()
        choice = input("Your choice: ")

        if choice == "0":
            break

        elif choice == "1":
            n1, m1 = read_positive_ints("Enter size of first matrix: ")
            print("Enter matrix:")
            A = read_matrix(n1, m1)

            n2, m2 = read_positive_ints("Enter size of second matrix: ")
            print("Enter matrix:")
            B = read_matrix(n2, m2)

            if n1 != n2 or m1 != m2:
                print("The operation cannot be performed.")
            else:
                print("The result is:")
                print_matrix(add_matrices(A, B, n1, m1))

        elif choice == "2":
            n, m = read_positive_ints("Enter size of matrix: ")
            print("Enter matrix:")
            matrix = read_matrix(n, m)

            while True:
                try:
                    k = float(input("Enter constant: "))
                    break
                except ValueError:
                    print("Invalid input, please try again")

            print("The result is:")
            print_matrix(multiply_by_constant(matrix, n, m, k))

        elif choice == "3":
            n1, m1 = read_positive_ints("Enter size of first matrix: ")
            print("Enter matrix:")
            A = read_matrix(n1, m1)

            n2, m2 = read_positive_ints("Enter size of second matrix: ")
            print("Enter matrix:")
            B = read_matrix(n2, m2)

            if m1 != n2:
                print("The operation cannot be performed.")
            else:
                print("The result is:")
                print_matrix(multiply_matrices(A, B, n1, m1, n2, m2))

        elif choice == "4":
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")
            t_choice = input("Your choice: ")

            n, m = read_positive_ints("Enter matrix size: ")
            print("Enter matrix:")
            matrix = read_matrix(n, m)

            if t_choice == "1":
                result = transpose_main(matrix, n, m)
            elif t_choice == "2":
                result = transpose_side(matrix, n, m)
            elif t_choice == "3":
                result = transpose_vertical(matrix, n, m)
            elif t_choice == "4":
                result = transpose_horizontal(matrix, n, m)
            else:
                print("Invalid choice")
                continue

            print("The result is:")
            print_matrix(result)

        elif choice == "5":
            n, m = read_positive_ints("Enter matrix size: ")
            print("Enter matrix:")
            matrix = read_matrix(n, m)

            if n != m:
                print("The operation cannot be performed.")
            else:
                det = determinant(matrix)
                if isinstance(det, float) and det.is_integer():
                    det = int(det)
                print("The result is:")
                print(det)

        elif choice == "6":
            n, m = read_positive_ints("Enter matrix size: ")
            print("Enter matrix:")
            matrix = read_matrix(n, m)

            if n != m:
                print("The operation cannot be performed.")
            else:
                inv = inverse_matrix(matrix)
                if inv is None:
                    print("This matrix doesn't have an inverse.")
                else:
                    print("The result is:")
                    print_matrix(inv)

        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    matrix_operations()