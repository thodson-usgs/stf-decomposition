# stf_decomposition
stf_decomposition: Seasonal-Trend decomposition using the Fast Fourier transform

# Installation
Installing stf_deocmposition can be done with pip installation syntax
```
pip install stf-decomposition
```
The package is tested on Python 3.7, 3.8 and 3.9.

# Getting Started
In order to use stf_decomposition you will need a time series dataset of type pandas DataFrame or pandas Series. You will also need to specify the following input variables:
- window: A window function for use during the Fast Fourier transoform process to reduce spectral leakage. 
The possible window functions to be inputs can be found in the [get_window](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.get_window.html) scipy documentation. 
- period: An integer indicating the period of the time series input data. 
The period must be specified by the user if the input data does not already have period.
Optional input variable:
- seasonal: An integer indicating the seasonal window of the time series input data. 
If no input is given than an optimization function will be run to find the seasonal window that produces the smallest correlation between the seasonal and trend decomposed components. 


# Example

# How it works

# Testing
