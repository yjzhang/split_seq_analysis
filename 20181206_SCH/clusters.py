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
labels_b = pd.read_csv('../../../80k_cluster_numbers.csv')
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

plt.figure(figsize=(15, 25))
sns.heatmap(cluster_counts/cluster_counts.sum(1)[:,np.newaxis],
            yticklabels=cluster_cell_types,
            vmin=0, vmax=1, linewidths=0.5)
plt.xlabel('UNCURL clusters')
plt.ylabel('Seurat clusters')
plt.title('SCH Cerebellum Clusters')
plt.savefig('uncurl_vs_seurat_clusters.png', dpi=200)



