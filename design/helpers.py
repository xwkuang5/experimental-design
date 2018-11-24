import numpy as np


def construct_latin_square(levels, balanced=True, randomized=False):
    """Construct a n x n latin square from the levels

    Args:
        levels (list)       : a list of levels of the factor
        balanced (bool)     : whether the latin square should be balanced
        randomized (bool)   : whether the latin square should be randomized

    Returns:
        square (list): a 2d list of permutation of the levels
    """

    n = len(levels)
    assert n != 0, "Number of levels must be greater than 0"

    if n % 2 == 0 or not balanced:
        indices = np.arange(n)

        if randomized:
            np.random.shuffle(indices)

        square = np.empty((n, n), dtype=np.int64)

        for shift in range(n):
            for i in range(n):
                square[shift, i] = indices[(i + shift) % n]
    else:
        indices = [0]

        for a, b in zip(
                range(1, 1 + (n - 1) // 2), reversed(
                    range(n - (n - 1) // 2, n))):
            indices += [a, b]

        square = np.empty((n, n), dtype=np.int64)

        for shift in range(n):
            for i in range(n):
                square[shift, i] = indices[(i + shift) % n]

        mirror = np.flip(square, axis=1)

        square = np.concatenate((square, mirror))

        if randomized:
            row_permutation = np.random.permutation(n * 2)
            col_permutation = np.random.permutation(n * 2)

            square = square[row_permutation]
            square = square[col_permutation]

    levels_as_numpy_array = np.array(levels)

    return np.stack([
        levels_as_numpy_array[permutation] for permutation in square
    ]).tolist()


if __name__ == '__main__':
    pass
