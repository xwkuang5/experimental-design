import numpy as np

def construct_latin_square(levels, randomized=False):
    """Construct a n x n latin square from the levels

    Rows are indexed by participants and columns are indexed by orders
    """

    n = len(levels)
    assert n != 0, "Number of levels must be greater than 0"

    indices = np.arange(n)

    if randomized:
        np.random.shuffle(indices)

    square = np.empty((n, n), dtype=np.int64)

    for shift in range(n):
        for i in range(n):
            square[shift, i] = indices[(i + shift) % n]
    
    levels_as_numpy_array = np.array(levels)

    return np.stack([levels_as_numpy_array[permutation] for permutation in square]).tolist()

def construct_balanced_latin_square(levels):

    n = len(levels)
    assert n != 0, "Number of levels must be greater than 0"

    if n % 2 == 0:
        return construct_latin_square(levels)