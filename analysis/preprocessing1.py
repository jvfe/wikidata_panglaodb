"""Reconciles tissues, cells, germ layers and organs, saving csv files for all matches returned"""

from wikidata_panglaodb.pre import (
    downloads_panglao,
    reconcile_more_types,
    chunk_dataframe,
)
from reconciler import reconcile
import pandas as pd


def main():

    data_urls = {
        "tissues": "https://raw.githubusercontent.com/oscar-franzen/PanglaoDB/master/data/metadata.txt",
        "genes": "https://raw.githubusercontent.com/oscar-franzen/PanglaoDB/master/data/genes.txt",
        "cells_organs_germlayers": "https://raw.githubusercontent.com/oscar-franzen/PanglaoDB/master/data/germ_layers.txt",
        "cells_w_descriptions": "https://raw.githubusercontent.com/oscar-franzen/PanglaoDB/master/data/cell_type_desc.txt",
    }

    tissues, genes, cells_organs_germlayers, cells_w_descriptions = downloads_panglao(
        data_urls
    )

    tissues.to_csv("data/panglaodb/tissues.csv", index=False)
    genes.to_csv("data/panglaodb/genes.csv", index=False)
    cells_organs_germlayers.to_csv(
        "data/panglaodb/cells_organs_germlayers.csv", index=False
    )
    cells_w_descriptions.to_csv("data/panglaodb/cells_w_descriptions.csv", index=False)

    types = {
        "tissue": "Q40397",
        "anatomical structure": "Q4936952",
        "cell type": "Q189118",
        "cell": "Q7868",
        "organ": "Q712378",
    }

    # Reconciling tissues againt types tissue (Q40397) and anatomical structure (Q4936952)
    # doing the same for germ layers
    print("Reconciling tissues and germ layers")
    results_tissues = []
    tissues_dfs = [tissues["tissue"], cells_organs_germlayers["germ_layer"]]
    for df in tissues_dfs:
        reconciled = reconcile_more_types(
            df, type_qids=[types["tissue"], types["anatomical structure"]],
        )
        results_tissues.append(reconciled)

    tissues_reconciled = pd.concat(results_tissues)
    tissues_reconciled.to_csv(
        "results/all_matches/reconciled_tissues_germlayers.csv", index=False
    )

    # Reconciling cells with types cell type (Q189118) and cell (Q7868)
    print("Reconciling cell types")
    cells_reconciled = reconcile_more_types(
        cells_organs_germlayers["cell_type"],
        type_qids=[types["cell type"], types["cell"]],
    )

    cells_reconciled.to_csv("results/all_matches/cells_reconciled.csv", index=False)

    # Reconciling organs with types organ (Q712378) and anatomical structure (Q4936952)
    print("Reconciling organs")
    organs_reconciled = reconcile_more_types(
        cells_organs_germlayers["organ"],
        type_qids=[types["organ"], types["anatomical structure"]],
    )

    organs_reconciled.to_csv("results/all_matches/organs_reconciled.csv", index=False)


if __name__ == "__main__":
    main()
