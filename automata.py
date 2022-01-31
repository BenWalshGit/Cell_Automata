"""Implementations of Lorenz 96 and Conway's
Game of Life on various meshes"""

import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def lorenz96(initial_state, nsteps):
    """
    Perform iterations of the Lorenz 96 update.

    Parameters
    ----------
    initial_state : array_like or list
        Initial state of lattice in an array of floats.
    nsteps : int
        Number of steps of Lorenz 96 to perform.

    Returns
    -------

    numpy.ndarray
         Final state of lattice in array of floats

    >>> x = lorenz96([8.0, 8.0, 8.0], 1)
    >>> print(x)
    array([8.0, 8.0, 8.0])

    >>> lorenz96([False, False, True, False, False], 3)
    array([True, False, True, True, True])

    # write your code here to replace return statement
    return NotImplemented
    """

    x_old = np.array(initial_state)
    x_new = np.zeros(x_old.shape)
    for j in range(nsteps):
        print (j, x_old)
        for i in range(len(x_old)):
            x = 1/101 * (100 * x_old[i] + (x_old[i-2] - x_old[(i+1) % len(x_old)]) * x_old[i-1] + 8)
            x_new[i] = x
        x_old = np.array(x_new)
    return x_new




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
                    counter +=1
                if (j+1) <= n_cols-1 and board[i][j+1]:
                    counter +=1
                if (i-1) >=0 and (j-1) >= 0 and board[i-1][j-1]:
                    counter += 1
                if (i-1) >=0 and board[i-1][j]:
                    counter +=1
                if (i-1) >=0 and (j+1) <= n_cols-1 and board[i-1][j+1]:
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
                if board[(i+1)%n_rows][(j-1)%n_cols]:
                    counter +=1
                if board[(i+1)%n_rows][(j)%n_cols]:
                    counter +=1
                if board[(i+1)%n_rows][(j+1)%n_cols]:
                    counter +=1
                if board[(i)%n_rows][(j-1)%n_cols]:
                    counter +=1
                if board[(i)%n_rows][(j+1)%n_cols]:
                    counter +=1
                if board[(i-1)%n_rows][(j-1)%n_cols]:
                    counter +=1
                if board[(i-1)%n_rows][(j)%n_cols]:
                    counter +=1
                if board[(i-1)%n_rows][(j+1)%n_cols]:
                    counter +=1

                

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


def life2colour(initial_state, nsteps):
    """
    Perform iterations of Conway's Game of Life on a doubly periodic mesh.

    Parameters
    ----------
    initial_state : array_like or list of lists
        Initial 2d state of grid in an array ints with value 1, 0, or 1.
        Values of -1 or 1 represent "on" cells of both colours. Zero
        values are "off".
    nsteps : int
        Number of steps of Life to perform.

    Returns
    -------

    numpy.ndarray
        Final state of grid in array of ints of value -1, 0, or 1.
    """

    # write your code here to replace this return statement
    return NotImplemented


def lifepent(initial_state, nsteps):
    """
    Perform iterations of Conway's Game of Life on
    a pentagonal tessellation.

    Parameters
    ----------
    initial_state : array_like or list of lists
        Initial state of grid of pentagons.
    nsteps : int
        Number of steps of Life to perform.

    Returns
    -------

    numpy.ndarray
         Final state of tessellation.
    """

    # write your code here to replace return this statement
    return NotImplemented

# Remaining routines are for plotting


def plot_lorenz96(data, label=None):
    """
    Plot 1d array on a circle

    Parameters
    ----------
    data: arraylike
        values to be plotted
    label:
        optional label for legend.


    """

    offset = 8

    data = np.asarray(data)
    theta = 2*np.pi*np.arange(len(data))/len(data)

    vector = np.empty((len(data), 2))
    vector[:, 0] = (data+offset)*np.sin(theta)
    vector[:, 1] = (data+offset)*np.cos(theta)

    theta = np.linspace(0, 2*np.pi)

    rings = np.arange(int(np.floor(min(data))-1),
                      int(np.ceil(max(data)))+2)
    for ring in rings:
        plt.plot((ring+offset)*np.cos(theta),
                 (ring+offset)*np.sin(theta), 'k:')

    fig_ax = plt.gca()
    fig_ax.spines['left'].set_position(('data', 0.0))
    fig_ax.spines['bottom'].set_position(('data', 0.0))
    fig_ax.spines['right'].set_color('none')
    fig_ax.spines['top'].set_color('none')
    plt.xticks([])
    plt.yticks(rings+offset, rings)
    plt.fill(vector[:, 0], vector[:, 1],
             label=label, fill=False)
    plt.scatter(vector[:, 0], vector[:, 1], 20)


def plot_array(data, show_axis=False,
               cmap=plt.cm.get_cmap('seismic'), **kwargs):
    """Plot a 1D/2D array in an appropriate format.

    Mostly just a naive wrapper around pcolormesh.

    Parameters
    ----------

    data : array_like
        array to plot
    show_axis: bool, optional
        show axis numbers if true
    cmap : pyplot.colormap or str
        colormap

    Other Parameters
    ----------------

    **kwargs
        Additional arguments passed straight to pyplot.pcolormesh
    """
    plt.pcolormesh(1*data[-1::-1, :], edgecolor='y',
                   vmin=-2, vmax=2, cmap=cmap, **kwargs)

    plt.axis('equal')
    if show_axis:
        plt.axis('on')
    else:
        plt.axis('off')


def plot_pent(x_0, y_0, theta_0, clr=0):
    """
    Plot a pentagram

    Parameters
    ----------
    x_0: float
        x coordinate of centre of the pentegram
    y_0: float
        y coordinate of centre of the pentegram
    theta_0: float
        angle of pentegram (in radians)
    """
    colours = ['w', 'r']
    s_1 = 1/np.sqrt(3)
    s_2 = np.sqrt(1/2)

    theta = np.deg2rad(theta_0)+np.deg2rad([30, 90, 165, 240, 315, 30])
    r_pent = np.array([s_1, s_1, s_2, s_1, s_2, s_1])

    x_pent = x_0+r_pent*np.sin(-theta)
    y_pent = y_0+r_pent*np.cos(-theta)

    plt.fill(x_pent, y_pent, ec='k', fc=colours[clr])


def plot_pents(data):
    """
    Plot pentagrams in Cairo tesselation, coloured by value

    Parameters
    ----------
    data: arraylike
        integer array of values
    """
    plt.axis('off')
    plt.axis('equal')
    data = np.asarray(data).T
    for row in range(data.shape[0]):
        for col in range(data.shape[1]):
            x_c = (row+1)//2+(row//2)*np.cos(np.pi/6)-(col//2)*np.sin(np.pi/6)
            y_c = (col+1)//2+(col//2)*np.cos(np.pi/6)+(row//2)*np.sin(np.pi/6)
            theta = (90*(row % 2)*((col + 1) % 2)
                     - 90*(row % 2)*(col % 2) - 90*(col % 2))
            clr = data[row, data.shape[1]-1-col]
            plot_pent(x_c, y_c, theta, clr=clr)
