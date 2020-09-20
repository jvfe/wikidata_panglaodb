from wikidata_panglaodb.quality import (
    get_number_of_statements_for_items,
    get_genes_item_quality,
)
from io import StringIO
import pandas as pd


def test_get_number_of_statements_for_items():

    test_item = get_number_of_statements_for_items(["Q42"], has_property="P31")

    prop_value = test_item["has_property"].to_list()

    expected = [True]

    assert prop_value == expected


def test_get_genes_item_quality():

    data = StringIO(
        """
    item,itemLabel,statements,ensg_wdt,entrez,ensg_panglao,species
    Q14905444,LCAT,56,ENSG00000213398,3931,ENSG00000213398,Homo sapiens
    Q14905455,DHCR7,40,ENSG00000172893,1717,ENSG00000172893,Homo sapiens
    Q14905473,VHL,35,ENSG00000134086,7428,ENSG00000134086,Homo sapiens
    Q14905494,PTPN11,40,ENSG00000179295,5781,ENSG00000179295,Homo sapiens
    Q14905499,BGN,34,ENSG00000182492,633,ENSG00000182492,Homo sapiens
    Q14905502,LNPEP,29,ENSG00000113441,4012,ENSG00000113441,Homo sapiens
    """
    )

    test_df = pd.read_csv(data)

    result = get_genes_item_quality(test_df)

    expected_columns = pd.DataFrame(
        {"has_ensg": [True for _ in range(6)], "has_entrez": [True for _ in range(6)]}
    )

    pd.testing.assert_frame_equal(result.iloc[:, 3:], expected_columns)
