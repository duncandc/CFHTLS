#!/usr/bin/python

#Author: Duncan Campbell
#Written: July 9, 2013
#Yale University
#Description: Read in fits CFHTLS photo-z PDZ and combine files.
#This is only need for the W1 field!  remember to move the other fields' fits
#files to the output directory for simplicity when reading in these files later
#data from: ftp://ftpix.iap.fr/pub/CFHTLS-zphot-T0007/

###packages###
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits

def main():
  filepath = '/scratch/dac29/output/processed_data/terapix/photo_z_catalogues/'
  filename = 'pdz_W1_270912.fits'
  hdulist = fits.open(filepath+filename, memmap=True)
  tbdata = hdulist[1].data

  #create a redshift array for the pdz info
  zaxis = np.empty([len(tbdata.columns[9:]),1])
  for i in range(0,300):
    zaxis[i]= float(tbdata.columns[i+9].name[1]+tbdata.columns[i+9].name[3:])/100.0

  pdz=np.array(tbdata[i][9:])
  pdz=pdz/float(sum(pdz))

  plt.figure()
  for i in range(0,100):
    pdz=np.array(tbdata[i][9:])
    pdz=pdz/float(sum(pdz))
    plt.plot(zaxis,pdz, 'b', linewidth=1, alpha=0.25)

  plt.ylabel('probability density')
  plt.xlabel('z')
  plt.show()

if __name__ == '__main__':
  main()
