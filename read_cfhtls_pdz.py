#!/usr/bin/python

#Author: Duncan Campbell
#Written: July 9, 2013
#Yale University
#Description: Read in fits CFHTLS photo-z PDZ and combine files.
#This is only need for the W1 field!  remember to move the other fields' fits
#files to the output directory for simplicity when reading in these files later
#data from: ftp://ftpix.iap.fr/pub/CFHTLS-zphot-T0007/

###packages###
import numpy as np
from astropy.io import fits
import gc


def main():
  ###make sure to change these when running in a new enviorment!###
  #location of data directory
  filepath = '/scratch/dac29/data/CFHTLS-T0007/photo_z_pdz/'
  #save data to directory...
  savepath = '/scratch/dac29/output/processed_data/terapix/photo_z_catalogues/'


  filename='pdz_W1_270912_part1.fits'
  hdulist1 = fits.open(filepath+filename, memmap=True)
  tbdata1 = hdulist1[1].data

  filename='pdz_W1_270912_part2.fits'
  hdulist2 = fits.open(filepath+filename, memmap=True)
  tbdata2 = hdulist2[1].data

  nrows1=tbdata1.shape[0]
  nrows2=tbdata2.shape[0]
  nrows=nrows1+nrows2
  print nrows

  #create a new table and merge the two tables
  hdu = fits.new_table(hdulist1[1].columns, nrows=nrows)
  for name in hdulist1[1].columns.names:
    hdu.data.field(name)[nrows1:]=tbdata2.field(name)
  #save new table to disk
  hdu.writeto(savepath+'pdz_W1_270912.fits', clobber=True)

  print 'done!  remember to copy W2, W3, and W4 to the output directory!'

if __name__ == '__main__':
  main()
