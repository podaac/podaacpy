from setuptools import setup, find_packages

setup(
    name='podaacpy',
    version='0.1',
    description='Shorten the distance between data and human.',
    author='PO.DAAC',
    author_email='TBD',
    url='https://github.com/podaac/podaacpy',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'xarray',
        'pyresample',
        'matplotlib',
        'cartopy',
        'pandas',
        'h5py',
        'netcdf4',
        'dask',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

