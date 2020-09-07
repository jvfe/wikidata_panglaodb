from wikidata_panglaodb.wdt import get_number_of_statements_for_items


def test_get_number_of_statements_for_items():

    test_item = get_number_of_statements_for_items(["Q42"], has_property="P31")

    prop_value = test_item["has_property"].to_list()

    expected = [True]

    assert prop_value == expected

