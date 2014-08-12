#!/usr/bin/python

#Author: Duncan Campbell
#Written: July 9, 2013
#Yale University
#Description: Read in IDL save files of the processed ds9 regions files for the 
#masks for CFHTLS from terapix

###packages###
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from scipy.io.idl import readsav
import gc


def main():
    ###make sure to change these when running in a new enviorment!###
    #location of data directory
    filepath = '/scratch/dac29/output/processed_data/megapipe/masks/'
    #save data to directory...
    savepath = '/scratch/dac29/output/processed_data/megapipe/masks/'
    #################################################################

    field = 'W1'
    print 'opening',field,'masks...'
    s=readsav(filepath+field+'_masks'+'.dat')
    keys = s.viewkeys()
    name = list(keys)[0]
    masks = s[name][0]

    #column names
    print masks.dtype.names

    #number of masks
    print len(masks['size'])


if __name__ == '__main__':
  main()
