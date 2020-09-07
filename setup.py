"""The setup script."""

from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

install_requirements = [
    "nltk",
    "pandas",
    "reconciler",
    "seaborn",
    "requests"
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="João Vitor F. Cavalcante / Tiago Lubiana Alves",
    author_email="jvfe@ufrn.edu.br",
    python_requires=">=3.7",
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Research compendium for the project 'Analysing the extent of cell type information present in Wikidata: A case study on PanglaoDB'",
    install_requires=install_requirements,
    license="BSD license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="tabular wikidata opendata linked-data ontology single-cell",
    name="wikidata_panglaodb",
    packages=find_packages(include=["wikidata_panglaodb", "wikidata_panglaodb.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/jvfe/wikidata_panglaodb",
    version="0.1.0",
    zip_safe=False,
)
