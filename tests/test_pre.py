from wikidata_panglaodb.pre import (
    downloads_panglao,
    reconcile_more_types,
    chunk_dataframe,
)
import pandas as pd

data_urls = {
    "tissues": "https://raw.githubusercontent.com/oscar-franzen/PanglaoDB/master/data/metadata.txt",
    "genes": "https://raw.githubusercontent.com/oscar-franzen/PanglaoDB/master/data/genes.txt",
    "cells_organs_germlayers": "https://raw.githubusercontent.com/oscar-franzen/PanglaoDB/master/data/germ_layers.txt",
    "cells_w_descriptions": "https://raw.githubusercontent.com/oscar-franzen/PanglaoDB/master/data/cell_type_desc.txt",
}


def test_downloads_panglaodb():

    result = downloads_panglao(data_urls)

    assert len(result) == 4


def test_reconcile_more_types():

    cells_organs_germlayers = pd.read_csv(
        data_urls["cells_organs_germlayers"],
        names=["cell_type", "germ_layer", "organ"],
    ).iloc[:5, 0]

    reconciled = reconcile_more_types(
        cells_organs_germlayers, type_qids=["Q7868", "Q189118"]
    )

    assert reconciled.shape[1] == 7
