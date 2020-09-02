from wikidata_panglaodb.pre import hello


def test_hello():

    string = hello()

    assert string == "Hello, Science!"
