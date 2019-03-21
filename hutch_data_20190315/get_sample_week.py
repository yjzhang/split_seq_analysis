#!/usr/bin/env python

import os
import sys
import numpy as np
import pandas as pd

path = sys.argv[1]

sample_week = ['0'] + ['week 4']*15 + ['week 8']*16 + ['control']*16
cell_metadata = pd.read_csv(os.path.join(path, 'cell_metadata.csv'))

sample_week_cells = np.array([sample_week[i] for i in cell_metadata.rnd1_well])
np.savetxt(os.path.join(path, 'sample_week.txt'), sample_week_cells, fmt='%s')
