#!/usr/bin/env python

# merge DGE matrices from multiple runs of split-seq
# joins on genes...

import os
import sys

import numpy as np
import pandas as pd
from scipy.io import mmread, mmwrite
from scipy import sparse

dirs = sys.argv[1:]
all_matrices = []
all_gene_tables = []

for path in dirs:
    genes = pd.read_csv(os.path.join(path, 'genes.csv'), index_col=0)
    genes.index = genes.gene_id
    genes = genes.drop('gene_id', axis=1)
    all_gene_tables.append(genes)
    matrix = mmread(os.path.join(path, 'DGE.mtx'))
    matrix = sparse.csc_matrix(matrix)
    all_matrices.append(matrix)
print('finished loading data')

print('creating combined gene table')
# create a new genes.csv table with all genes
new_gene_table = pd.concat(all_gene_tables, axis=1)
# there has to be a better way to do this...
# https://stackoverflow.com/questions/31828240/first-non-null-value-per-row-from-a-list-of-pandas-columns
new_gene_table.gene_name = new_gene_table.gene_name.bfill(axis=1).iloc[:, 0]
new_gene_table.genome = new_gene_table.genome.bfill(axis=1).iloc[:, 0]
new_gene_table = new_gene_table.iloc[:,:2]
print('finished creating combined gene table')

new_gene_table.to_csv('combined_gene_table.csv')
new_gene_table.gene_name.to_csv('combined_gene_names.txt', index=None)

# for each matrix, update it to include a 0 column for every gene that wasn't originally included
new_matrices = []
for g, m in zip(all_gene_tables, all_matrices):
    print('updating matrix...')
    cells = m.shape[0]
    new_m = m.copy()
    index = 0
    gene_ids = set(g.index)
    for gene_id, row in new_gene_table.iterrows():
        if gene_id not in gene_ids:
            m_left = new_m[:, :index]
            m_right = new_m[:, index:]
            new_m = sparse.hstack([m_left, sparse.csc_matrix((cells, 1)), m_right])
        index += 1
    new_matrices.append(new_m)
print('finished updating matrices')

# concatenate all new matrices and write it out
new_matrix = sparse.vstack(new_matrices)
mmwrite('combined_dge.mtx', new_matrix)
print('finished writing combined matrix')

# concatenate cell_metadata
print('combining cell metadata')
all_cell_metadata = []
all_sample_ids = []
for path in dirs:
    all_cell_metadata.append(pd.read_csv(os.path.join(path, 'cell_metadata.csv'), index_col=None))
    sample_id = '_'.join(path.split('_')[:-1])
    print(sample_id)
    all_sample_ids += [sample_id]*len(all_cell_metadata[-1])

combined_cell_metadata = pd.concat(all_cell_metadata)
combined_cell_metadata['sample_id'] = all_sample_ids
combined_cell_metadata.to_csv('combined_cell_metadata.csv', index=None)

combined_cell_metadata.sample_id.to_csv('combined_sample_ids.txt', index=None)
