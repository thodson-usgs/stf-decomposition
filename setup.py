import setuptools

setuptools.setup(
    name="stf-decomposition",
    version="0.1",
    description="seasonal-trend decomposition using the Fast Fourier transform in python",
    long_description=   "Fast decomposition of timeseries into trend, seasonal, and residual"
                        "components using the FFT."
                        ""
                        "For docs and more information, "
                        "visit the Github repo at "
                        "https://github.com/thodson-usgs/stf-decomposition.",
    long_description_content_type="text/markdown",
    url="https://github.com/thodson-usgs/stf-decomposition",
    author="Timothy O. Hodson",
    author_email="thodson@usgs.gov",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=setuptools.find_packages(),
    install_requires=["scipy", "pandas",],
)
