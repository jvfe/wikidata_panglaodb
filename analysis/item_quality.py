# %% [markdown]
# # Analysing item matches and item quality


# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wikidata_panglaodb.wdt import get_number_of_statements_for_items

sns.set(style="whitegrid", palette="muted")

# %%
cells = pd.read_csv("results/true_matches/cells.csv")
organs = pd.read_csv("results/true_matches/organs.csv")
tissues = pd.read_csv("results/true_matches/tissues.csv")
mmu_genes = pd.read_csv("results/true_matches/mus_musculus_genes.csv")
hsa_genes = pd.read_csv("results/true_matches/homo_sapiens_genes.csv")
# %%
cells_w_statements = get_number_of_statements_for_items(
    cells["id"].to_list(), has_property="P7963"
)
cells_w_statements["class"] = "Cell Type"
organs_w_statements = get_number_of_statements_for_items(
    organs["id"].to_list(), has_property="P1554"
)
organs_w_statements["class"] = "Organ"
tissues_w_statements = get_number_of_statements_for_items(
    tissues["id"].to_list(), has_property="P1554"
)
tissues_w_statements["class"] = "Tissue"

histology_items = pd.concat(
    [cells_w_statements, organs_w_statements, tissues_w_statements]
)

# PLOT IDEAS #
# Barplot for each item type - Number of statements/has alternative ids ?
# Distribution of number of statements for each item type
