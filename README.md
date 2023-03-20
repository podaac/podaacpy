# podaac science-enabling routines
A test podaacpy package that contains commonly used functions for search and access the PODAAC products. Some of the future development will include for example
1. regridding level-2 swath data onto uniform lat-lon or Cartesian coordinates.
2. global regridding using HealPix
3. API to machine learning code to do ocean eddy detection, cloud-gap filling etc.

This package is under development. No stability guarantee. 


## Installation

You can install the package using pip:
```
   pip install podaac
```
Try: 
```
   from podaac import utils
   utils.find_dataset(keywords=['NOAA','SST'])
   utils.find_dataset(keywords=['NOAA','SST','2P'])
   utils.find_dataset(keywords=['OSCAR'])
```
