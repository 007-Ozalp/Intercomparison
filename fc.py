import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def computeSenSlopeMap(seasonalMapsNcFile, outputNcFile):
    
    inputDs = xr.open_dataset(seasonalMapsNcFile)        
##vals: per input data Summer and Winter Season Files
##a method for robust linear regression. It computes the slope as the median of all slopes (all seasonal mean) between paired values.
    def _compSenSlope(vals):
        alpha = .95
        medslope, _, _, _ = stats.mstats.theilslopes(vals, alpha=alpha)
        return medslope
###Apply a vectorized function for unlabeled arrays on xarray objects.
###xarray.apply_ufunc
###The function will be mapped over the data variable(s) of the input arguments 

    slp = xr.apply_ufunc(_compSenSlope, inputDs, input_core_dims=[["time"]], dask="allowed", vectorize=True)
    #slp_10=slp*36
    slp.to_netcdf(outputNcFile)
    print("Output:", slp)
    return slp,inputDs

def computeAnomaly(from_time,to_time,selectMonth):
    # input = xr.open_dataset(inputnc,engine='netcdf4')
    print("Insert to select a date from time:",from_time)
    print("Insert to select a date to time:",to_time)
    print("Insert a Month to calculate Anomaly:",selectMonth)

    return from_time,to_time,selectMonth
