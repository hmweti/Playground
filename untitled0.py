# -*- coding: utf-8 -*-
"""
Created on Thu May 11 13:14:54 2017

@author: hmweti
"""

import gdal

infile = "inputfile.tif"
data   = gdal.Open(infile)

print data