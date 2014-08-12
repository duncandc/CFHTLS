#!/usr/bin/python

#Author: Duncan Campbell
#Written: July 9, 2013
#Yale University
#Description: Read in IDL save files of the processed ds9 regions files for the 
#masks for CFHTLS from terapix and save as numpy files

###packages###
import numpy as np
from scipy.io.idl import readsav


def main():
    masks_cat = 'megapipe'
    ###make sure to change these when running in a new enviorment!###
    #location of data directory
    filepath = '/scratch/dac29/output/processed_data/'+masks_cat+'/masks/'
    #save data to directory...
    savepath = '/scratch/dac29/output/processed_data/'+masks_cat+'/masks/'
    #################################################################

    fields = ['W1','W2','W3','W4']

    field = fields[3]
    print 'opening',field,'masks...'
    s=readsav(filepath+field+'_masks'+'.dat')
    keys = s.viewkeys()
    name = list(keys)[0]
    masks = s[name][0]

    #column names
    print masks.dtype.names
    print type(masks['ra'])

    #number of masks
    print len(masks['size'])

    filename = field+'_masks'
    np.save(savepath+filename, masks)


if __name__ == '__main__':
  main()
