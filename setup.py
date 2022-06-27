#! /usr/bin/env python
#
# Copyright (C) 2012-2022 Michael Waskom

DESCRIPTION = "seaborn: statistical data visualization"
LONG_DESCRIPTION = """\

Seaborn is a library for making statistical graphics in Python. It is built on
top of `matplotlib <https://matplotlib.org/>`_ and closely integrated with
`pandas <https://pandas.pydata.org/>`_ data structures.

Here is some of the functionality that seaborn offers:

- A dataset-oriented API for examining relationships between multiple variables
- Flexible data aggregation with automatic estimation and plotting of error bars
- Multiple options for visualizing univariate or bivariate distributions
- Estimation and plotting of linear regression models to reveal trends
- Tools for building figures with multidimensional views onto complex dataset structure
- Concise control over matplotlib figure styling with several built-in themes
- Tools for choosing color palettes that faithfully reveal patterns in your data

Seaborn aims to make visualization a central part of exploring and understanding
data. Its dataset-oriented plotting functions operate on dataframes and arrays
containing whole datasets and internally perform the necessary semantic mapping
and statistical aggregation to produce informative plots.

"""

DISTNAME = 'seaborn'
MAINTAINER = 'Michael Waskom'
MAINTAINER_EMAIL = 'mwaskom@gmail.com'
URL = 'https://seaborn.pydata.org'
LICENSE = 'BSD (3-clause)'
DOWNLOAD_URL = 'https://github.com/mwaskom/seaborn/'
VERSION = '0.12.0b1'
PYTHON_REQUIRES = ">=3.7"

INSTALL_REQUIRES = [
    'numpy>=1.17',
    'pandas>=0.25',
    'matplotlib>=3.1',
    'typing_extensions; python_version < "3.8"',
]

EXTRAS_REQUIRE = {
    'all': [
        'scipy>=1.3',
        'statsmodels>=0.10',
    ]
}


PACKAGES = [
    'seaborn',
    'seaborn._core',
    'seaborn._marks',
    'seaborn._stats',
    'seaborn.colors',
    'seaborn.external',
]

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'License :: OSI Approved :: BSD License',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Multimedia :: Graphics',
    'Operating System :: OS Independent',
    'Framework :: Matplotlib',
]


if __name__ == "__main__":

    from setuptools import setup

    import sys
    if sys.version_info[:2] < (3, 7):
        raise RuntimeError("seaborn requires python >= 3.7.")

    setup(
        name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        python_requires=PYTHON_REQUIRES,
        install_requires=INSTALL_REQUIRES,
        extras_require=EXTRAS_REQUIRE,
        packages=PACKAGES,
        classifiers=CLASSIFIERS
    )
