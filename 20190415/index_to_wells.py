# converts back and forth between well index numbers and well ids of the form "A1", "A2", etc.

def rnd1_index_to_well(index):
    """
    Args:
        index (int)

    Returns: string of format '[A-D][1-12]'
    """
    row_letters = ['A', 'B', 'C', 'D']
    x1 = index/12
    x2 = index%12
    return row_letters[x1] + str(x2 + 1)

def rnd1_well_to_index(well):
    """
    Args:
        well (str): format is '[A-D][1-12]'

    Returns: integer between 0 and 47
    """
    row_letters = {'A':0, 'B':1, 'C':2, 'D':3}
    x1 = well[0]
    index = row_letters[x1]
    return index

if __name__ == '__main__':
    import pandas as pd
    data = pd.read_csv('DGE_filtered/cell_metadata.csv')
    group1_indices = [0,1,2,12,13,14,24,25,26,36,37,38]
    group2_indices = [3,4,5,15,16,17,27,28,29,39,40,41]
    group3_indices = [6,7,8,18,19,20,30,31,32,42,43,44]
    group4_indices = [9,10,21,22,33,45]
    group5_indices = [11,23,34,35,46,47]
    index1 = [(x in group1_indices) for x in data.rnd1_well]
    index2 = [(x in group2_indices) for x in data.rnd1_well]
    index3 = [(x in group3_indices) for x in data.rnd1_well]
    index4 = [(x in group4_indices) for x in data.rnd1_well]
    index5 = [(x in group5_indices) for x in data.rnd1_well]

