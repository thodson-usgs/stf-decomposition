---
title: 'STF: Seasonal-Trend decomposition using the Fast Fourier transform in Python'
tags:
  - Python
  - seasonal-trend decomposition
  - statistics
authors:
  - name: Katherine J. Miles 
    orcid: 0000-0002-2790-3969
    affiliation: "1, 2" 
  - name: Timothy O. Hodson
    orcid: 0000-0003-0962-5130
    affiliation: "1" 
affiliations:
 - name: U.S. Geological Survey Central Midwest Water Science Center
   index: 1
 - name: University of Illinois
   index: 2
date: 1 July 2022
bibliography: paper.bib

---

# Summary
Seasonal-Trend Decomposition is a commonly used to break time series data into distinct seasonal, trend, and residual components. By breaking time series data into these distinct components it is easier to distinguish the underlying patterns of the data associated with long-term trends or associated with short-term seasonal fluctuations. 
# Statement of Need
Seasonal-Trend Decompositions are widely used across a variety of fields. Fields where time series data is commonplace such as economics or hyrdologic geology benefit from seasonal-trend decompositions to better understand the vast amount of time series data. Various seasonal trend decomposition methods exist and can be accessed through Python or R libraries such as Seasonal-Trend Decomposition using Regression (STR) and Seasonal-Trend Decomposition using LOESS (STL). While the STR and STL methods are easily accessible, they can become computationally slow if used with large datasets. The Seasonal-Trend decomposition using the Fast Fourier transform allows for decreased computation time as compared to STR and STL. With the STF() python library, fast and accurate seasonal-trend decompositions can be computed even with very large time series datasets. 

# Example

# How It Works

# Features

The package includes the following features:

- Feature 1
- Feature 2

The package can be downloaded through the [Python Package Index](https://pypi.org/project/stf-decomposition/).
The full code is publicly available on [github](https://github.com/thodson-usgs/stf-decomposition).
Documentation, including an API reference, can be found at [Read The Docs](https://stf-decomposition.readthedocs.io/en/latest/).

# Acknowledgements

Funding for this research was provided by the Hydro-terrestrial Earth Systems Testbed (HyTEST) project of the U.S. Geological Survey Integrated Water Prediction program.
Any use of trade, firm, or product names is for descriptive purposes only and does not imply endorsement by the U.S. Government.

# References