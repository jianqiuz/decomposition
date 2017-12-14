import numpy as np
import math as math
from writephrq import *

fldoc   = 0.01
fsom1   = 0.01
fsom2   = 0.02
fsom3   = 0.10
fmic    = 1.0e-6

sldoc   = 0.8

ffe3    = 0.02

kfera   = 0.5
kferh   = 0.8
kmega   = 0.6
kmegh   = 0.5

kdecay  = 0.1


fferb  = fmic*0.01
fmega  = fmic*2
fmegh  = fmega
 
totc = [0.2584,0.1438]                #mol  total organic carbon
totw = [0.0049, 0.0058] #kg   water
tots = [3.13, 4.21]                #g    soil dry mass
ph   = [5.055, 5.305]
cace = [39.87, 2.84]                #mM   acetate T and P measured value
cfe2 = [25.62, 20.92]                #mM   Fe
hdsp = [0.051, 0.051] #head space volume L
 
index = 0
writephrq('hto', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferb, fmega, fmegh, sldoc)
 
writephrq('hto',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
		ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferb, fmega, fmegh, sldoc)

writephrq('hto',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferb, fmega, fmegh, sldoc)
 
index = 1
writephrq('htm', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferb, fmega, fmegh, sldoc)
 
writephrq('htm',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferb, fmega, fmegh, sldoc)
 
writephrq('htm',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferb, fmega, fmegh, sldoc)
 
