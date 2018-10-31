# coding: utf-8

import numpy as np
import pandas as pd
import scipy.io

data_spinal_cord = scipy.io.mmread('spinal_cord.mtx.gz')

from scipy import sparse

data_spinal_cord = sparse.csc_matrix(data_spinal_cord)
first_five_cells = data_spinal_cord[:, 0:5]
genes = np.loadtxt('genes.txt', dtype=str)
genes = [x.upper() for x in genes]
first_five_cells = first_five_cells.toarray().astype(int)

df = pd.DataFrame({'genes': genes, 'Cell 1': first_five_cells[:,0], 'Cell 2': first_five_cells[:,1], 'Cell 3': first_five_cells[:,2], 'Cell 4': first_five_cells[:,3], 'Cell 5': first_five_cells[:,4]})

df = df[['genes', 'Cell 1', 'Cell 2', 'Cell 3', 'Cell 4', 'Cell 5']]
df.to_csv('data_for_cellSearchAtlas.csv', index=None)
