#!/usr/bin/python

#Author: Duncan Campbell
#Written: June 24, 2013
#Yale University
#Description: Read in hdf5 CFHTLS photo-z catalogues and print out names

###packages###
import numpy as np
from astropy.io import ascii
import h5py


def main():
  ###make sure to change these when running in a new enviorment!###
  #location of data directory
  filepath = '/scratch/dac29/output/processed_data/terapix/photo_z_catalogues/'
  #################################################################

  field = 'test'
  f =  h5py.File(filepath+field+'.hdf5', 'r')
  dset = f.get('test')
  print dset.shape
  f.close

  dset_arr=np.array(dset)
  for gal in dset_arr['ID']:
    print gal

if __name__ == '__main__':
  main()
