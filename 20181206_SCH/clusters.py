# coding: utf-8

from uncurl_analysis.sc_analysis import SCAnalysis
sca = SCAnalysis('tmp/uncurl/c88bac6d-d1c6-4c58-b3b7-9934a8cfcb26-20181216_SCH_80k_real')
sca = sca.load_params_from_folder()
sca.labels
len(sca.labels)

sca.cell_sample
sca.cell_subset
sca.cell_subset.shape
labels = sca.w.argmax(0)

from sklearn.metrics.cluster import normalized_mutual_info_score as nmi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
labels_b = pd.read_csv('80k_cluster_numbers.csv')
labels_b = labels_b.iloc[:,1]
labels_b = labels_b.values
labels_b_subset = labels_b[sca.cell_subset]
nmi(labels_b_subset, labels)

from sklearn.metrics.cluster import adjusted_rand_score as ari
ari(labels_b_subset, labels)

cluster_counts = np.zeros((len(set(labels_b)), len(set(labels))))
for i, j in zip(labels_b_subset, labels):
    cluster_counts[i, j] += 1

plt.figure(figsize=(10, 25))
sns.heatmap(cluster_counts/cluster_counts.sum(1)[:,np.newaxis],
            yticklabels=sorted(list(set(labels_b_subset))),
            vmin=0, vmax=1, linewidths=0.5)
plt.xlabel('UNCURL clusters')
plt.ylabel('Seurat clusters')
plt.title('SCH Cerebellum Clusters')
plt.savefig('uncurl_vs_seurat_clusters.png', dpi=200)

cluster_file = pd.read_csv('80k_clustering_master_file - All_Integrated_res1.csv')
cluster_file = cluster_file.iloc[:,3:]
cluster_cell_types = [str(i) + ' ' + str(cluster_file[str(i)][0]) for i in range(33)]
cluster_cell_types.append('33')

plt.figure(figsize=(15, 25))
sns.heatmap(cluster_counts/cluster_counts.sum(1)[:,np.newaxis],
            yticklabels=cluster_cell_types,
            vmin=0, vmax=1, linewidths=0.5)
plt.xlabel('UNCURL clusters')
plt.ylabel('Seurat clusters')
plt.title('SCH Cerebellum Clusters')
plt.savefig('uncurl_vs_seurat_clusters.png', dpi=200)

# do a biclustering

from sklearn.cluster.bicluster import SpectralCoclustering

spec = SpectralCoclustering(18)
cluster_counts_subset = np.vstack([cluster_counts[:31, :], cluster_counts[32:,:]])
spec.fit(cluster_counts + 0.0001)
row_labels = spec.row_labels_
column_labels = spec.column_labels_

row_order = np.argsort(row_labels)
col_order = np.argsort(column_labels)

#row_labels = row_labels[row_order]
#col_labels = column_labels[col_order]

cluster_counts_reordered = cluster_counts[row_order, :]
cluster_counts_reordered = cluster_counts_reordered[:, col_order]
cluster_cell_types_2 = np.array([str(x) + ': ' + y for x, y in zip(row_labels, cluster_cell_types)])
col_labels = np.array([str(x) + ': ' + str(y) for x, y in zip(column_labels, range(len(column_labels)))])

plt.figure(figsize=(25, 30))
ax = sns.heatmap(cluster_counts_reordered/cluster_counts_reordered.sum(1)[:,np.newaxis],
            yticklabels=cluster_cell_types_2[row_order],
            xticklabels=col_labels[col_order],
            vmin=0, vmax=1)
prev_label = 0
for i, c in enumerate(row_labels[row_order]):
    if c != prev_label:
        ax.axhline(i, linewidth=3)
        prev_label = c
prev_label = 0
for i, c in enumerate(column_labels[col_order]):
    if c != prev_label:
        ax.axvline(i, linewidth=3)
        prev_label = c
plt.xlabel('UNCURL clusters')
plt.ylabel('Seurat clusters')
plt.title('SCH Cerebellum Clusters')
plt.savefig('uncurl_vs_seurat_clusters_coclustering.png', dpi=150)


# do a biclustering
from sklearn.cluster.bicluster import SpectralBiclustering

spec = SpectralBiclustering(20)
cluster_counts_subset = np.vstack([cluster_counts[:31, :], cluster_counts[32:,:]])
spec.fit(cluster_counts + 0.0001)
row_labels = spec.row_labels_
column_labels = spec.column_labels_

row_order = np.argsort(row_labels)
col_order = np.argsort(column_labels)

#row_labels = row_labels[row_order]
#col_labels = column_labels[col_order]

cluster_counts_reordered = cluster_counts[row_order, :]
cluster_counts_reordered = cluster_counts_reordered[:, col_order]
cluster_cell_types_2 = np.array([str(x) + ': ' + y for x, y in zip(row_labels, cluster_cell_types)])
col_labels = np.array([str(x) + ': ' + str(y) for x, y in zip(column_labels, range(len(column_labels)))])

plt.figure(figsize=(20, 25))
sns.heatmap(cluster_counts_reordered/cluster_counts_reordered.sum(1)[:,np.newaxis],
            yticklabels=cluster_cell_types_2[row_order],
            xticklabels=col_labels[col_order],
            vmin=0, vmax=1, linewidths=0.5)
plt.xlabel('UNCURL clusters')
plt.ylabel('Seurat clusters')
plt.title('SCH Cerebellum Clusters')
plt.savefig('uncurl_vs_seurat_clusters_biclustering.png', dpi=200)


