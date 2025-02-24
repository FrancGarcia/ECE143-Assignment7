def count_paths(m,n,blocks):
    """
    Return the number of paths you can take from starting index of 0,0 to ending index of m-1,n-1 within the given grid.
    The path is 0-index and contains # to represent a block that you cannot pass and a . that denotes you can pass.
    You can only travel through the grid by going right or by going down the grid.

    :param m: The number of rows in the grid
    :param n: The number of columns in the grid
    :param blocks: The list of tuples that represent where a # block is located
    
    :return: The number of paths you can go from start to end in the grid by only going down and right.
    """
    assert(isinstance(m, int) and m >= 0), "Number of rows must be an integer at least 0"
    assert(isinstance(n, int) and n >= 0), "Number of columns must be an integer at least 0"
    assert(isinstance(blocks, list)), "Blocks must be a valid list"
    for block in blocks:
        assert(isinstance(block, tuple)), "Each block in blocks must be a tuple"
        assert(isinstance(block[0], int) and block[0] >= 0), "First entry of current block must be a type int of at least 0"
        assert(isinstance(block[1], int) and block[1] >= 0), "Second entry of current block must be a type int of at least 0"
    res = [[0] * n for _ in range(m)]
    res[0][0] = 1
    print(res)
    for r in range(m):
        for c in range(n):
            if (r,c) not in blocks:
                if 1 <= r < m and 1 <= c < n:
                    res[r][c] = res[r-1][c] + res[r][c-1]
                elif 1 <= r < m:
                    res[r][c] = res[r-1][c]
                elif 1 <= c < n:
                    res[r][c] = res[r][c-1]
    print(res)
    return res[m-1][n-1]

blocks = [(0,3),(1,1)]
count_paths(3,4,blocks)

