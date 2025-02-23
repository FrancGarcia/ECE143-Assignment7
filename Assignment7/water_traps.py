def get_trapped_water(seq):
    """
    Given the list of unit heights, returns the number of units of water
    trapped between all walls of the map which is represented as the seq list.
    
    :param seq: The list of integers that represents the height of that wall.
    :return: The units of water trapped in between the walls in the map.
    """
    assert(isinstance(seq, list)), "Argument must be a list"
    for height in seq:
        assert(height >= 0 and isinstance(height,int)), "Heights in seq must be integers of at least 0"
    
    l = len(seq)
    m_l = float('-inf')
    m_r = float('-inf')
    left_max = [0]*l
    right_max = [0]*l
    for i in range(l):
        if seq[i] > m_l:
            m_l = seq[i]
        if seq[l-1-i] > m_r:
            m_r = seq[l-1-i]
        left_max[i] = m_l
        right_max[l-1-i] = m_r
    trapped_amt = 0
    for i in range(l):
        trapped_amt += min(left_max[i], right_max[i]) - seq[i]
    return trapped_amt