import itertools
import numpy as np
def solvefrob(coefs,b):
    """
    Solves the Frobenius equation. The coefficients are represented as the coefs list
    that is passed in. The Frobenius equation is in the form a_1 x_1 +... + a_n x_n = b.
    
    :param coefs: The list of a_i coefficients in the Frobenius equation.
    :param b: The positive constant integer that we use to solve the x_i coefficients for.
    """
    assert(isinstance(b, int) and b > 0), "b must be a valid integer greater than 0"
    assert(isinstance(coefs, list)), "coefs must be a list"
    for coef in coefs:
        assert(isinstance(coef, int) and coef > 0), "coef must be a valid integer greater than 0"
    quotients = b//np.array(coefs)
    ranges = [np.arange(q+1).tolist() for q in quotients]
    combinations = np.array(list(itertools.product(*ranges)))
    solutions = combinations[np.dot(combinations,coefs) == b]
    return [tuple(int(num) for num in solution) for solution in solutions]
