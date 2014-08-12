#!/usr/bin/python

#Author: Duncan Campbell
#Written: June 24, 2013
#Yale University
#Description: Read in ascii CFHTLS photo-z catalogues and save as HDF5 files.
#data from: ftp://ftpix.iap.fr/pub/CFHTLS-zphot-T0007/

###packages###
import numpy as np
from astropy.io import ascii
import h5py
import gc


def main():
  ###make sure to change these when running in a new enviorment!###
  #location of data directory
  filepath = '/scratch/dac29/data/CFHTLS-T0007/photo_z_catalogues/'
  #save data to directory...
  savepath = '/scratch/dac29/output/processed_data/terapix/photo_z_catalogues/'
  #################################################################
  
  #column names
  names=['ID','ra','dec','flag','StarGal','r2','final photo-z','zPDF', \
         'zPDF_168','zPDF_u68','chi2_zPDF','mod','ebv', \
         'NbFilt','zMin','z168','zu68','chi2_best','zp_2','chi_2','mods', \
         'chis','zq','chiq','modq','U','G','R','I','Y','Z','eU','eG','eR', \
         'eI','eY','eZ','MU','MG','MR','MI','MY','MZ']

  #here is a small file to test the code with#
  field = 'test'
  print 'reading in:',field
  filename = 'test.out'
  data = ascii.read(filepath+filename, delimiter='\s', names=names, \
                    guess=False, Reader=ascii.Basic)
  f = h5py.File(savepath+field+'.hdf5', 'w')
  dset = f.create_dataset(field, data=data)
  f.close()
  gc.collect()

  #here is the real deal, fields 1 through 4
  field='W1'
  print 'reading in:',field
  filename = 'photozCFHTLS-W1_270912.out'
  data = ascii.read(filepath+filename, delimiter='\s', names=names, \
                    guess=False, Reader=ascii.Basic)
  f = h5py.File(savepath+field+'.hdf5', 'w')
  dset = f.create_dataset(field, data=data)
  print dset.shape
  f.close()
  gc.collect()

  sys.exit()

  field='W2'
  print 'reading in:',field
  filename = 'photozCFHTLS-W2_270912.out'
  data = ascii.read(filepath+filename, delimiter='\s', names=names, \
                    guess=False, Reader=ascii.Basic)
  f = h5py.File(savepath+field+'.hdf5', 'w')
  dset = f.create_dataset(field, data=data)
  f.close()
  gc.collect()

  field='W3'
  print 'reading in:',field
  filename = 'photozCFHTLS-W3_270912.out'
  data = ascii.read(filepath+filenam3, delimiter='\s', names=names, \
                    guess=False, Reader=ascii.Basic)
  f = h5py.File(savepath+filename[-4]+'.hdf5', 'w')
  dset = f.create_dataset(field, data=data)
  f.close()
  gc.collect()

  field='W4'
  print 'reading in:',field
  filename = 'photozCFHTLS-W4_270912.out'
  data = ascii.read(filepath+filename, delimiter='\s', names=names, \
                    guess=False, Reader=ascii.Basic)
  f = h5py.File(savepath+field+'.hdf5', 'w')
  dset = f.create_dataset(field, data=data)
  f.close()
  gc.collect()

if __name__ == '__main__':
  main()
