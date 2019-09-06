# Programming exercise 1

import os
import numpy as np
import pandas as pd

def create_directory_from_path(direc):
  """
  Loads directory structure with CSV files into directory

  Parameters
  ----------
  direc : str
      Path to directory to be converted to dictionary

  Returns
  ----------
  ds : dictionary
      Directory modelled as a dictionary
  """
  ds = {}
  for i in os.listdir(direc):
    path = os.path.join(direc, i)
    if os.path.isfile(path): continue # continue if file in root
    ds[i] = {}
    for j in os.listdir(path):
      if os.path.splitext(j)[1] == '.csv': # Select only files with given extension
        with open(os.path.join(path, j)) as data:
          keys = j.replace('.csv','')
          df = pd.read_csv(data)
          print(df)
          #variables = {'x1'}
          #ds[i].update()
  return ds

direc = os.getcwd() + "/dataset" # Get current working directory
ds = create_directory_from_path(direc)

# use pseudoinverse when calculating the MSE to avoid zero in denominator
# pinv() in numpy

# 1. Implement linear regression with ordinary least squares (OLS) using the
# closed-form solution seen in Equation 9.

# Load variables
#x = ds['regression']['train_1d_reg_data'][:,0]
#y = ds['regression']['train_1d_reg_data'][:,0]

#print(vals[:,0])

# find weight that gies the OLS
#w = np.linalg.pinv( x1.transpose().dot(x1) ).dot( x1.transpose().dot(y) )

#print(w)
