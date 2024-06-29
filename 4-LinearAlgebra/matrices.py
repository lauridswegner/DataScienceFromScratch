from typing import List, Tuple, Callable

Matrix = List[List[float]]
Vector = List[float]

A = [[1,2,3],       # has 2 rows and 3 columns
     [4,5,6]]

B = [[1,2],         # has 3 rows and 2 columns
     [3,4],
     [5,6]]

def shape(A: Matrix) -> Tuple[int, int]:
    """Return (# of Rows A, # of Columns A)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

assert shape([[1,2,3], [4,5,6]]) == (2,3)

def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of A (as a Vector)"""
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    """Returns the j-th column of A (as a Vector)"""
    return [A_i[j]          # j-th element of row A_i
            for A_i in A]   # for each row A_i

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Returns a num_rows x num_cols matrix
    whose (i,j)-th entry is entry_fn(i,j)
    """
    return [[entry_fn(i, j)             # given i, create a list
             for j in range(num_cols)]  #   [entry_fn(i, 0), ... ]
             for i in range(num_rows)]  # create one list for each i

def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]