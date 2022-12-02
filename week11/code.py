#!/usr/bin/env python
import scanpy as sc
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import rc_context
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)
  
#sc.tl.pca(adata)
#sc.pl.pca(adata)

sc.pp.neighbors(adata,n_neighbors=10,n_pcs=40)
sc.tl.leiden(adata)

#code for umap plot
fig, ax = plt.subplots()
sc.tl.umap(adata, maxiter=1000)
sc.pl.umap(adata, color='leiden', ax=ax, show=False)
fig.tight_layout()
fig.savefig("umap.png")

#code for tsne
fig, ax = plt.subplots()
sc.tl.tsne(adata)
sc.pl.tsne(adata,color='leiden',ax=ax, show=False)
fig.tight_layout()
fig.savefig("tsne.png")

#code for rank genes groups by two method

sc.tl.rank_genes_groups(adata,groupby='leiden', method='logreg')
sc.tl.rank_genes_groups(adata,groupby='leiden', method='t_test')
sc.pl.rank_genes_groups_dotplot(adata,groupby='leiden')

#draw a dotplot to find marker genes
sc.tl.rank_genes_groups(adata,groupby='leiden', method='logreg')
sc.pl.rank_genes_groups_dotplot(adata, n_genes=4)

#according to the dotplot, we can identify marker genes in each clusters.So I search those genes in the database and find which cluster they belong to. And I identify that: cluster 22(Trp73) is EC2 cell groups; cluster 24(Abcc9) is PC;cluster16(Hbb-bt)is Ec3; cluster 26(Maf) is MG; cluster20 is OL(olig1); cluster 25(c1qb) is MG)
cluster_anno={'20':'OL','22':'EC2','24':'PC','16':'EC33','26':'MG','25':'MG'}
adata.obs['cell type'] = adata.obs['leiden'].map(cluster_anno).astype('category')
sc.tl.umap(adata, maxiter=1000)
sc.pl.umap(adata, color=['Trp73','Abcc9','Hbb-bt','Maf','Olig1','C1qb'],s=50, frameon=False, ncols=4)

