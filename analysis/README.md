# Analysis directory

Here you will find all scripts used in the actual analysis. To run them,
make sure you ran `pip install .` at the root directory.

## Brief description

* **preprocessing.py**: Downloads metadata from PanglaoDB into the data/panglaodb directory, also reconciles said data and outputs 
    the matches to the results/all_matches directory.

* **similarity_check.py**: Checks the reconciled/all_matches data for similarity matching, outputting the filtered data to results/true_matches.