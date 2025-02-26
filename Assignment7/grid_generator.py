import numpy as np
import random
def gen_rand_slash(m=6,n=6,direction='back'):
    """
    Generates a random slash in a m x n numpy array with at least
    two pixels. The slash can be "back" or "forward" slash.

    :param m: Number of rows in the numpy image.
    :param n: Number of columns in the numpy image.
    :param direction: "back" or "forward" to determine the direction of the slash generated.
    
    :return: An m x n numpy array with the randomly generated slash.
    """
    assert(isinstance(m, int) and m > 1), "The number of columns (i.e. m) must be an int greater than 1 to get uniform slash"
    assert(isinstance(n, int) and n > 1), "The number of rows (i.e. n) must be an int greater than 1 to get uniform slash"
    assert(isinstance(direction, str) and (direction == "back" or direction == "forward")), "The direction must be 'back' or 'forward' only"
    
    slash = np.array([[0 for _ in range(n)] for _ in range(m)])
    if direction == "back":
        start_ind_r = random.randint(0,m-2)
        start_ind_c = random.randint(0,n-2)
        l = min(m-start_ind_r, n-start_ind_c)
        length = random.randint(2, l)
        move = 1
    elif direction == "forward":
        start_ind_r = random.randint(1,m-1)
        start_ind_c = random.randint(0,n-2)
        l = min(start_ind_r+1,n-start_ind_c)
        length = random.randint(2, l)
        move = -1
    count = 0
    while count < length:
        slash[start_ind_r, start_ind_c] = 1
        start_ind_r += move
        start_ind_c += 1
        count += 1
    return slash