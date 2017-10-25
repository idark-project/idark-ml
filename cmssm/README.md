# Global fits of GUT-scale SUSY models with GAMBIT
* [Zenodo page ](https://zenodo.org/record/843496)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.843496.svg)](https://doi.org/10.5281/zenodo.843496)
* [arXiv:1705.07935](https://arxiv.org/abs/arXiv:1705.07935)
* [Dataset](https://zenodo.org/record/843496/files/CMSSM.hdf5.tar.gz)

## How to download and prepare the dataset

The dataset is too large to host on github. Here's step-by-step intructions on how retrieve the data and prepare it.

1. Download the Gambit's CMSSM [dataset from Zenodo](https://zenodo.org/record/843496/files/CMSSM.hdf5.tar.gz). **Warning**, it's 10 GB download, and 31 GB uncompressed.
2. Uncompress and place the file in this directory (path should be cmssm/CMSSM.hdf5, relative to repository root.)
3. Run `python extract_columns.py` to construct CMSSM_subset.hdf5.
4. Done.


# References 
* [https://arxiv.org/pdf/1709.02249.pdf](https://arxiv.org/pdf/1709.02249.pdf)
* [Drop-out as Bayesian Approximation](https://arxiv.org/abs/1506.02142), there's a series of papers on this topic from Yarin Gal.
* [Blog introduction to Mixture Density Networks](http://blog.otoro.net/2015/06/14/mixture-density-networks/)
* [Bishop on Mixture Density Networks](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bishop-ncrg-94-004.pdf)
