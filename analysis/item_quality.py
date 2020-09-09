# %% [markdown]
# # Analysing item matches and item quality


# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from wikidata_panglaodb.quality import get_number_of_statements_for_items

sns.set(style="whitegrid", palette="muted")

# %%
cells = pd.read_csv("results/true_matches/cells_checked.csv").drop_duplicates(
    subset=["id"]
)
organs = pd.read_csv("results/true_matches/organs_checked.csv").drop_duplicates(
    subset=["id"]
)
tissues = pd.read_csv("results/true_matches/tissues_checked.csv").drop_duplicates(
    subset=["id"]
)
mmu_genes = pd.read_csv("results/true_matches/mus_musculus_genes.csv")
hsa_genes = pd.read_csv("results/true_matches/homo_sapiens_genes.csv")
# %%
cells_w_statements = get_number_of_statements_for_items(
    cells["id"].to_list(), has_property="P7963"
)
organs_w_statements = get_number_of_statements_for_items(
    organs["id"].to_list(), has_property="P1554"
)
tissues_w_statements = get_number_of_statements_for_items(
    tissues["id"].to_list(), has_property="P1554"
)

histology_items = pd.concat(
    [cells_w_statements, organs_w_statements, tissues_w_statements]
)

# PLOT IDEAS #
# Barplot for each item type - Number of statements/has alternative ids ?
# Distribution of number of statements for each item type
# %%


def get_genes_item_quality(df, drop=True):

    result_df = df.copy().rename(columns={"item": "id"})

    result_df["has_ensg"] = np.where(result_df["ensg_wdt"].isna(), False, True)
    result_df["has_entrez"] = np.where(result_df["entrez"].isna(), False, True)

    if drop == True:
        result_df.drop(["itemLabel", "ensg_wdt", "ensg_panglao"], axis=1, inplace=True)

    return result_df


# %%
gene_items = pd.concat(
    [get_genes_item_quality(mmu_genes), get_genes_item_quality(hsa_genes)]
)


# %%
