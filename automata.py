"""Implementations of Conway's Game of Life"""

import numpy as np
import pprint


def life(initial_state, nsteps):
    """
    Perform iterations of Conway’s Game of Life.
    Parameters
    ----------
    initial_state : array_like or list of lists
        Initial 2d state of grid in an array of booleans.
    nsteps : int
        Number of steps of Life to perform.
    Returns
    -------
    numpy.ndarray
         Final state of grid in array of booleans
    """

    board = np.array(initial_state)
    n_rows = board.shape[0]
    n_cols = board.shape[1]

    for k in range(nsteps):
        new_board = np.array(board)
        for i in range(n_rows):
            for j in range(n_cols):

                counter = 0
                if (i+1) <= n_rows-1 and (j-1) >= 0 and board[i+1][j-1]:
                    counter += 1
                if (i+1) <= n_rows-1 and board[i+1][j]:
                    counter += 1
                if (i+1) <= n_rows-1 and (j+1) <= n_cols-1 and board[i+1][j+1]:
                    counter += 1
                if (j-1) >= 0 and board[i][j-1]:
                    counter += 1
                if (j+1) <= n_cols-1 and board[i][j+1]:
                    counter += 1
                if (i-1) >= 0 and (j-1) >= 0 and board[i-1][j-1]:
                    counter += 1
                if (i-1) >= 0 and board[i-1][j]:
                    counter += 1
                if (i-1) >= 0 and (j+1) <= n_cols-1 and board[i-1][j+1]:
                    counter += 1

                if board[i][j]:
                    if counter == 2 or counter == 3:
                        new_board[i][j] = True
                    else:
                        new_board[i][j] = False

                if board[i][j] == False:
                    if counter == 3:
                        new_board[i][j] = True
                    else:
                        new_board[i][j] = False

        board = np.array(new_board)

    return board


def life_periodic(initial_state, nsteps):
    """
    Perform iterations of Conway's Game of Life on a doubly periodic mesh.

    Parameters
    ----------
    initial_state : array_like or list of lists
        Initial 2d state of grid in an array of booleans.
    nsteps : int
        Number of steps of Life to perform.

    Returns
    -------

    numpy.ndarray
         Final state of grid in array of booleans
    """
    board = np.array(initial_state)
    n_rows = board.shape[0]
    n_cols = board.shape[1]

    for k in range(nsteps):
        new_board = np.array(board)
        for i in range(n_rows):
            for j in range(n_cols):

                counter = 0
                if board[(i+1) % n_rows][(j-1) % n_cols]:
                    counter += 1
                if board[(i+1) % n_rows][(j) % n_cols]:
                    counter += 1
                if board[(i+1) % n_rows][(j+1) % n_cols]:
                    counter += 1
                if board[(i) % n_rows][(j-1) % n_cols]:
                    counter += 1
                if board[(i) % n_rows][(j+1) % n_cols]:
                    counter += 1
                if board[(i-1) % n_rows][(j-1) % n_cols]:
                    counter += 1
                if board[(i-1) % n_rows][(j) % n_cols]:
                    counter += 1
                if board[(i-1) % n_rows][(j+1) % n_cols]:
                    counter += 1

                if board[i][j]:
                    if counter == 2 or counter == 3:
                        new_board[i][j] = True
                    else:
                        new_board[i][j] = False

                if board[i][j] == False:
                    if counter == 3:
                        new_board[i][j] = True
                    else:
                        new_board[i][j] = False

        board = np.array(new_board)

    return board


# Here is a test for the periodic function called the blinker test.
# The 3 middle horizontal 'Trues' turn vertical after 1 step! 
test_board_blinker = np.array([[False, False, False, False, False],
                               [False, False, False, False, False],
                               [False, True, True, True, False],
                               [False, False, False, False, False],
                               [False, False, False, False, False]])

print(life_periodic(test_board_blinker, 1))

# Here is a similar test for the normal life function, except the shape of
# 'Trues' should shift one upward and one to the right after 4 runs!
test_board_glider = np.array([[False, False, False, False, False],
                                [False, True, True, True, False],
                                [False, False, False, True, False],
                                [False, False, True, False, False],
                                [False, False, False, False, False]])

print(life(test_board_glider, 4))
