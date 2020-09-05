# %%
from wikidata_panglaodb.similarity import get_string_match

# %%
string1 = "Dopaminergic neurons"
string2 = "dopaminergic cell group"


# %%
get_string_match(string1, string2)
