# Cerebellum data analysis

Dataset: embryonic cerebellum tissue

URL: http://ec2-34-213-89-36.us-west-2.compute.amazonaws.com:8888/user/82d142e7-4b6b-4811-8434-ad6c79949180-SeattleChildrens-cerebell/view

With the $k=10$ dataset, after 1 split, we have 11 clusters.

## Data overview

![summary.png](summary.png "Data summary")

The data consists of [n] cells and [m] genes.

Filtering was done to exclude cells with fewer than 500 or more than 10000 reads.

## Splitting/merging

Pre-splitting/merging processed and unprocessed views:

![01.png](01.png "pre-splitting cluster 0 processed view")

![02.png](02.png "pre-splitting cluster 0 unprocessed view")

First, we split cluster 0. This was because the cluster clearly separated out into two separate clusters in the unprocessed view. After splitting, the two output clusters resolved themselves into cluster 0 and cluster 1.

After the first split:

![post_split_c0.png](post_split_c0.png "post-splitting cluster 0 unprocessed view")

![post_split_c0_processed.png](post_split_c0_processed.png "post-splitting cluster 0 processed view")

Next, we split cluster 3. This is a large cluster with 1038 cells, and in the unprocessed view, it seems to be split into two distinct blobs.

After the second split:

![post_split_c3.png](post_split_c3.png "post-splitting cluster 3 unprocessed view")

![post_split_c3_processed.png](post_split_c3_processed.png "post-splitting cluster 3 processed view")

## Entropy


![entropy_processed.png](entropy_processed.png "Entropy processed view")

![entropy_unprocessed.png](entropy_unprocessed.png "Entropy unprocessed view")

When running Uncurl, "entropy" essentially denotes how uncertain a cell's classification is. In both of these views, we can see a high entropy region near the center of the plot, surrounded by low-entropy groups of cells. This indicates that there is a significant population of cells for which the cell type identification is uncertain.

## Cluster 0

![cluster_0_top_genes.png](cluster_0_top_genes.png "cluster 0 top genes")

This is a relatively large cluster, with 1040 cells. In both the processed and unprocessed tSNE plots, it appears to be relatively homogeneous, although the processed view shows a small portion that connects with cluster 7.

The top 1-vs-rest genes are GRID2, QKI, NCKAP5, and NPAS3, all with fold-changes of greater than 2.

### Enrichr results

with the top 10 1-vs-rest genes:

ARCHS4_tissues: Fetal brain, Midbrain, Prefrontal Cortex (not very helpful...)

GO_Biological_Process: nervous system development, excitatory postsynaptic potential (this would indicate that these cells represent neurons - excitatory neurons in particular)

### Top gene descriptions

GRID2: https://www.genecards.org/cgi-bin/carddisp.pl?gene=GRID2 - "Glutamate Ionotropic Receptor Delta Type Subunit 2" - these code for excitatory neurotransmitter receptors.

QKI:

### Assignment

**excitatory neuron**


## Cluster 1 (original)

This is the orange cluster.

This cluster seems to show some heterogeneity in the unprocessed plot, so it was split.

## Cluster 1 (new)

### Enrichr results

### Top gene descriptions

RORA
