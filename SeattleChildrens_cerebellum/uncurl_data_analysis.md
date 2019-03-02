# Cerebellum data analysis

Dataset: embryonic cerebellum tissue

URL: <http://ec2-54-149-220-127.us-west-2.compute.amazonaws.com:8888/user/d909e044-63cc-4b2a-942b-0611b0be4837-cerebellum-k10-all-cells/view>

With starting $k=10$, after 4 splits, we have 14 clusters.

## Data overview

![summary.png](summary.png "Data summary"){ width=800px }

The data consists of [n] cells and [m] genes.

Filtering was done to exclude cells with fewer than 500 or more than 10000 reads.

## Splitting/merging

Pre-splitting/merging processed and unprocessed views:

![01.png](01.png "pre-splitting cluster 0 processed view"){ width=800px }

![02.png](02.png "pre-splitting cluster 0 unprocessed view"){ width=800px }

First, we split cluster 0. This was because the cluster clearly separated out into two separate clusters in the unprocessed view. After splitting, the two output clusters resolved themselves into cluster 0 and cluster 1.

After the first split:

![post_split_c0.png](post_split_c0.png "post-splitting cluster 0 unprocessed view"){ width=800px }

![post_split_c0_processed.png](post_split_c0_processed.png "post-splitting cluster 0 processed view"){ width=800px }

Next, we split cluster 3. This is a large cluster with 1038 cells, and in the unprocessed view, it seems to be split into two distinct blobs.

After the second split:

![post_split_c3.png](post_split_c3.png "post-splitting cluster 3 unprocessed view"){ width=800px }

![post_split_c3_processed.png](post_split_c3_processed.png "post-splitting cluster 3 processed view"){ width=800px }

The next cluster to split was cluster 9. Despite being a relatively small cluster with 670 cells, it seemed to show a good deal of heterogeneity in the unprocessed view. In addition, all of the top genes are mitochondrial genes.

After the third split:

![post_split_c9.png](post_split_c9.png "post-splitting cluster 9 unprocessed view"){ width=800px }

![post_split_c9_processed.png](post_split_c9_processed.png "post-splitting cluster 9 processed view"){ width=800px }


The next cluster to split would be cluster 2. This cluster seems to have genes that separate out into multiple blobs. And the gene expression patterns also show substantial differences.

After the fourth split:

![post_split_c2.png](post_split_c2.png "post-splitting cluster 2 unprocessed view"){ width=800px }

![post_split_c2_processed.png](post_split_c2_processed.png "post-splitting cluster 2 processed view"){ width=800px }

The next cluster to split would probably be cluster 6. The is the largest remaining cluster, with 1057 cells, but it seems to have pretty good "blob coherence" (a newly coined technical term) in both views, with low entropy in the bulk of its assigned cells. Also, it does not seem to have differences in gene expression patterns.

So that's the end of the splits.

(UNCURL TODO: it would be a good idea to get some sense of "cluster coherence", similar to the inter-cluster distance, but for similarity within a cluster. The entropy metric sort of gets that, but its interpretation for clustering purposes is somewhat subjective.)

## Entropy

After all the splits were done, the entropy looks like this:

![entropy_processed.png](entropy_processed.png "Entropy processed view"){ width=800px }

![entropy_unprocessed.png](entropy_unprocessed.png "Entropy unprocessed view"){ width=800px }

When running Uncurl, "entropy" essentially denotes how uncertain a cell's classification is. In both of these views, we can see a high entropy region near the center of the plot, surrounded by low-entropy groups of cells. This indicates that there is a significant population of cells for which the cell type identification is uncertain.

High entropy could also correspond to doublets in sequencing or other technical errors. Currently Uncurl is not yet capable of decomposing biological and technical variation, but it might be possible to make some guesstimates?


## Cluster 0

![cluster_0_top_genes.png](cluster_0_top_genes.png "cluster 0 top genes"){ width=400px }

571 cells

### Enrichr results

with the top 10 1-vs-rest genes:

ARCHS4_tissues: Cerebellum, Cerebral cortex, motor neuron, spinal cord

GO_Biological_Process: Positive regulation of histone H3-K4 methylation, positive rgulation of transcription

### Top gene descriptions

I got these from genecards.org.

RORA: "RAR Related Orphan Receptor A" - transcriptional regulator, involved in circadian rhythm. nuclear receptor.

AUTS2: "Autism susceptibility candidate 2" - a transcriptional regulator gene that does chromatin remodeling and modification of histones.

DAB1: "Dap Reelin signal transducer" - this regulates neuron positioning and organization in the developing brain, helping neurons reach the correct layer in the cortex.

HS6ST3: "Heparan Sulfate 6-O-Sulfotransferase 3" - modifies Heparan sulfate, which is a polysaccharide.

FOXP2: "Forkhead box protein P2" - apparently pretty important, has a wikipedia page. Called the "language gene" because it has role in language disorders, is involved in brain development. This is a transcription factor.

NRXN3: "Neurexin 3" - involved as a receptor, cell adhesion?

NPAS3: "Neuronal PAS Domain Protein 3" - localized to nucleus and may be involved in neurogenesis. transcription factor activity.

CA8: "Carbonic Anhydrase 8" - mutations are associated with neurologic defect in mice? no known activity?

NTM: "Neurotrimin" - neuronal cell adhesion

CHST11: "Carbohydrate Sulfotransferase 11"

Top c-score genes not found in 1-vs-rest: most of these had pretty low effect c-scores - the highest c-score was about 1.5.

(TODO for uncurl: it might be nice to have a gene set explorer view - visualize relationships between genes, relationships between genes and other terms. Could use existing gene networks or build a new one by literature mining?)


### Assignment

immature/developing/undifferentiated neuron? pre-differentiated cells similar to cluster 1?

Reasoning: most overexpressed genes are transcription factors, involved in development


## Cluster 1

![cluster_1_top_genes.png](cluster_1_top_genes.png "cluster 1 top genes"){ width=400px }

468 cells


### Enrichr results

with the top 10 1-vs-rest genes:

ARCHS4_tissues: Cerebellum, cerebral cortex, sensory neuron, motor neuron

GO_Biological_Process: glutamate receptor signaling pathway, cellular protein localization

### Top gene descriptions

DAB1: seen above

RORA: seen above

EBF1: "Early B Cell Factor 1" - this is a transcription factor. also called "olfactory neuronal transcription factor 1".

KCNIP4: "Potassium Channel Interacting Protein 4" - this regulates voltage-gated potassium channels.

GRID2: "Glutamate Ionotropic Receptor Delta Type Subunit 2" - glutamate receptors are excitatory neurotransmitter receptors.

DMD: "Dystrophin" - contains actin-binding domains, involved in cytoskeleton? intracellular transport?

ITPR1: "Inositol 1,4,5-Trisphosphate Receptor Type 1" - mediates calcium release from the endoplasmic reticulum.

FOXP2: see above

AUTS2: see above

GRIK1: "Glutamate Ionotropic Receptor Kainate Type Subunit 1" - this is another glutamate receptor type (excitatory receptor)

top c-score genes were ITPR1, EBF1, DMD, GRIK1, KCNIP4, SDK1, DAB1, IL1RAPL2, IMMP2L, BAI3.

SDK1: "Sidekick Cell Adhesion Molecule 1" - provides synaptic connectivity?

IL1RAPL2: "Interleukin 1 Receptor Accessory Protein Like 2" - associated with X-linked diseases?

IMMP2L: "Inner Mitochondrial Membrane Peptidase Subunit 2"

BAI3: "Brain-specific angiogenesis inhibitor 3"

### Assignment

**Excitatory neuron**?

## Cluster 2

![cluster_2_top_genes.png](cluster_2_top_genes.png "cluster 2 top genes"){ width=400px }

253 cells

### Enrichr results

with the top 10 1-vs-rest genes:

ARCHS4_tissues: Dentate granule cell, alpha cell, dorsal striatum, cerebral cortex, beta cell

GO_Biological_Process: regulation of potassium ion transmembrane transport, leukocyte chemotaxis, activation of protein kinase activity, negative regulation of cell death

### Top gene descriptions

MT-RNR2: "Mitochondrially Encoded 16S RNA" - non-coding RNA - apparently a "neuroprotective factor" - suppresses apoptosis

RNA28S5: "RNA, 28S Ribosomal 5" - ribosomal RNA

MT-RNR1: "Mitochondrially Encoded 12S RNA" - non-coding RNA, associated with deafness?

C4orf22: "Cilia and flagella associated protein 299"

C12orf55: "Cilia And Flagella Associated Protein 54"

DPP10: "Dipeptidyl Peptidase Like 10" - membrane protein - promotes cell surface expression of potassium channel.

AGBL4: "ATP/GTP Binding Protein Like 4"

DNAH9: "Dynein Axonemal Heavy Chain 9" - molecular motor - attaches to microtubles, movement of cilia and flagella

PACRG: "Parkin Coregulated" - chaperone protein. Associated with Parkinson's disease. Localized to epithelia, also asociated with cilia.

WDR96: "Cilia And Flagella Associated Protein 43" 

Top c-score genes: C12orf55, C4orf22, DNAH9, WDR96, TMEM232, SPAG17, DNAH7, PACRG, AGBL4, HYDIN

TMEM232: "Transmembrane Protein 232"

SPAG17: "Sperm associated antigen 17" - function associated with cilia.

HYDIN: also associated with cilial motility. 

### Assignment

**Ependymal/Epithelial?**

According to wikipedia, Ependymal cells have cilia. So these are probably ependymal cells given how many cilia genes there are.

What does it mean when most of the top genes are mitochondrial RNAs? That the cell has some high-energetic activity?

## Cluster 3

![cluster_3_top_genes.png](cluster_3_top_genes.png "cluster 3 top genes"){ width=400px }

300 cells

### Enrichr results

with the top 10 1-vs-rest genes:

ARCHS4_tissues:

GO_Biological_Process:

### Top gene descriptions

SOX2-OT: "SOX2 Overlapping Transcript (Non-Protein Coding)"

PTPRZ1: "Protein Tyrosine Phosphatase, Receptor Type Z1" - "may be involved in the regulation of specific developmental processes in the CNS" - negatively regulates oligodendrocyte precursor proliferation - required for differentiation of precursors into fully myelinating oligodendrocytes.

LSAMP: "Limbic System-Associated Membrane Protein" -this is a neuronal surface protein, may act as adhesion, neuronal growth, axon targeting. tumor suppressor?

CSMD1: "CUB And Sushi Multiple Domains 1" - associated with some kinds of epilepsy?

LRP1B: LDL Receptor related Protein 1B 

LRRC4C: "Leucine Rich Repeat Containing 4C" - "May promote neurite outgrowth of developing thalamic neurons"

NPAS3: see above

LHFPL3: "LHFPL Tetraspan Subfamily Member 3" - transmembrane protein - associated with deafness - associated with gliomas?

KCND2: "Potassium Voltage-Gated Channel Subfamily D Member 2" 

OPCML: "Opioid Binding Protein/Cell Adhesion Molecule Like" - membrane receptor. Downregulated in brain gliomas?

Top c-score genes: SOX2-OT, PTPRZ1, SOX6, PDE4B, PCDH15, LHFPL3, MMP16, LRP1B, LSAMP, TNR

SOX6: transcription factor

PDE4B: "Phosphodiesterase 4B" - regulates cAMP concentrations

PCDH15: "Protocadherin Related 15" - membrane protein that mediates cell-cell adhesion. Associated with deafness.

MMP16: "Matrix Metallopeptidase 16"

### Assignment

Glial cells - endothelial?

Potentially: Oligodendrocyte, oligodendrocyte precursors (due to PTPRZ1)???


## Cluster 4

![cluster_4_top_genes.png](cluster_4_top_genes.png "cluster 4 top genes"){ width=400px }

512 cells

### Enrichr results

with the top 10 1-vs-rest genes:

ARCHS4_tissues: cerebellum, dorsal striatum, fetal brain, oligodendrocyte, cerebral cortex

GO_Biological_Process: regulation of ventricular cardiac muscle cell action potential, bundle of His cell-Purkinje myocyte adhesion involved in cell communication , response to light stimulus, muscle cell development

### Top gene descriptions

GRID2: see above

NCKAP5: "NCK Associated Protein 5" - also called "peripheral clock protein" - associated with hypersomnia.

QKI: see above

NPAS3: see above

PTN: Pleiotrophin - this is a heparin-binding growth factor. induces neuritite growth?

CTNNA3: "Catenin Alpha 3" - Cadherin-associated protein - associated with cell-cell adhesion.

GRIA1: "Glutamate Ionotropic Receptor AMPA Type Subunit 1" - another excitatory neurotransmitter receptor.

LSAMP: "Limbic System-Associated Membrane Protein" -this is a neuronal surface protein, may act as adhesion, neuronal growth, axon targeting. tumor suppressor?

C-score top genes: CTD-3088G3.8, NCKAP5, TNC, CTNNA3, SLC1A3, PTN, MAPK10, MEIS1, SLC35F1, MEGF10

TNC: "Tenascin C" - extracellular matrix protein - associated with guidance of migrating neurons and axons.

SLC1A3: "Solute Carrier Family 1 Member 3" - glutamate transporter protein. functions in termination of excitatory neurotransmission.

MAPK10: MAP Kinase 10 - associated with neuronal proliferation signalling pathways.

MEIS1: Meis Homeobox 1 - 



### Assignment

Excitatory neuron

## Cluster 5

![cluster_5_top_genes.png](cluster_5_top_genes.png "cluster 5 top genes"){ width=400px }


### Enrichr results

with the top 10 1-vs-rest genes:

ARCHS4_tissues:

GO_Biological_Process:

### Top gene descriptions


### Assignment


## Cluster 6

![cluster_6_top_genes.png](cluster_6_top_genes.png "cluster 6 top genes"){ width=400px }


### Enrichr results

with the top 10 1-vs-rest genes:

ARCHS4_tissues:

GO_Biological_Process:

### Top gene descriptions


### Assignment



## Cluster 7

![cluster_7_top_genes.png](cluster_7_top_genes.png "cluster 7 top genes"){ width=400px }


### Enrichr results

with the top 10 1-vs-rest genes:

ARCHS4_tissues:

GO_Biological_Process:

### Top gene descriptions


### Assignment



## Cluster 8

![cluster_8_top_genes.png](cluster_8_top_genes.png "cluster 8 top genes"){ width=400px }


### Enrichr results

with the top 10 1-vs-rest genes:

ARCHS4_tissues:

GO_Biological_Process:

### Top gene descriptions


### Assignment



## Cluster 9

![cluster_9_top_genes.png](cluster_9_top_genes.png "cluster 9 top genes"){ width=400px }


### Enrichr results

with the top 10 1-vs-rest genes:

ARCHS4_tissues:

GO_Biological_Process:

### Top gene descriptions


### Assignment



## Cluster 10

![cluster_10_top_genes.png](cluster_10_top_genes.png "cluster 10 top genes"){ width=400px }


### Enrichr results

with the top 10 1-vs-rest genes:

ARCHS4_tissues:

GO_Biological_Process:

### Top gene descriptions


### Assignment


## Cluster 11 
![cluster_11_top_genes.png](cluster_11_top_genes.png "cluster 11 top genes"){ width=400px }


### Enrichr results

with the top 10 1-vs-rest genes:

ARCHS4_tissues:

GO_Biological_Process:

### Top gene descriptions


### Assignment


## Cluster 12

![cluster_12_top_genes.png](cluster_12_top_genes.png "cluster 12 top genes"){ width=400px }


### Enrichr results

with the top 10 1-vs-rest genes:

ARCHS4_tissues:

GO_Biological_Process:

### Top gene descriptions


### Assignment


## Cluster 13

![cluster_13_top_genes.png](cluster_13_top_genes.png "cluster 13 top genes"){ width=400px }


### Enrichr results

with the top 10 1-vs-rest genes:

ARCHS4_tissues:

GO_Biological_Process:

### Top gene descriptions


### Assignment

