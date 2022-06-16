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
Seasonal-Trend Decomposition are commonly used to break time series data into distinct seasonal, trend, and residual components.
By breaking time series data into these distinct components it is easier to distinguish the underlying patterns of the data associated with long-term trends or associated with short-term seasonal fluctuations. 
# Statement of Need
Seasonal-Trend Decompositions are widely used across a variety of fields. 
Fields where time series data is commonplace such as economics or hyrdologic geology benefit from seasonal-trend decompositions 
to better understand the vast amount of time series data. 
Various seasonal trend decomposition methods exist and can be accessed through Python or R libraries
such as Seasonal-Trend Decomposition using Regression (STR) and Seasonal-Trend Decomposition using LOESS (STL).
While the STR and STL methods are easily accessible, they can become computationally slow if used with large datasets. 
The Seasonal-Trend decomposition using the Fast Fourier transform allows for decreased computation time as compared to STR and STL. 
With the STF() python library, fast and accurate seasonal-trend decompositions can be computed even with very large time series datasets. 

# Example
A time series data set of historical CO2 emission rates was used as an example input for stf_decomposition.
The first step in the stf_decomposition workflow is to create an stf_decomposition object.
For this example the inputs to create the stf_decomposition object were the CO2 data set, 
a window specification of "Blackman", and a seasonal adjuster of 13.
After the stf_decomposition object is created, you can call the fit() method that will compute the individual decomposed signal components.
The plot() method was then called on the fitted object which plotted the seasonal, trend, and residual decompositions as well as the original data. 
From the plots, we can see that the long-term, linear upward trend has been extracted from the oscillating seasonal trends. 

![CO2 Example](Example.png)

# How It Works

# Features

The package includes the following features:

- Feature 1
- Feature 2

The package can be downloaded through the [Python Package Index](https://pypi.org/project/stf-decomposition/).
The full code is publicly available on [github](https://github.com/thodson-usgs/stf-decomposition).
Documentation, including an API reference, can be found at [Read The Docs](https://stf-decomposition.readthedocs.io/en/latest/).

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }

# Acknowledgements

Funding for this research was provided by the Hydro-terrestrial Earth Systems Testbed (HyTEST) project of the U.S. Geological Survey Integrated Water Prediction program.
Any use of trade, firm, or product names is for descriptive purposes only and does not imply endorsement by the U.S. Government.

# References
