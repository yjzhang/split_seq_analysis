#!/usr/bin/env python3

import numpy as np
from scipy.io import loadmat

# load the latest Seattle Children's dataset
data_mat = loadmat('20181206_SCH_80kcells_novaseq_v2.mat')

# this is a cells x genes sparse matrix in CSC format
dge = data_mat['DGE']

# genes is a list of strings corresponding to gene names
genes = data_mat['genes']

# find all intronic genes
intronic_genes = np.array(['INTRONIC' in x for x in genes])

# subset data and genes to non-intronic
dge_subset = dge[:, ~intronic_genes]
genes_subset = genes[~intronic_genes]

# rename genes to remove '_HUMAN'
genes_renamed = np.array([x.split('_')[0] for x in genes_subset])

# save data subset
from scipy.io import mmwrite
dge_subset = dge_subset.T
mmwrite('20181206_SCH_80kcells_novaseq_v2_non_intronic.mtx', dge_subset)

# save gene names
np.savetxt('20181206_SCH_80kcells_novaseq_v2_gene_names.txt', genes_renamed, '%s')
