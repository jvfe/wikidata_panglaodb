from wikidata_panglaodb.similarity import get_string_match


def test_get_string_match():

    string1 = "Dopaminergic neurons"
    similar_to_one = "dopaminergic neuron"
    not_similar = "cholinergic neuron"

    assert get_string_match(string1, similar_to_one) == True
    assert get_string_match(string1, not_similar) == False
