import numpy as np
import math as math
from writephrq import *

fldoc   = 0.02
fsom1   = 0.1
fsom2   = 0.4
fsom3   = 0.1
fmic    = 1e-6
fmicp   = 1.0e-7

sldoc   = 0.8

ffe3    = 0.02

kfera   = 0.5
kferh   = 0.8
kmega   = 0.6
kmegh   = 0.5

kdecay  = 0.1


fferb  = fmic*10
fmega    = fmic*10
fmegh  = fmega

fferbp  = fmicp*5
fmegap    = fmicp*2
fmeghp  = fmegap
 
totc = [0.1611, 0.0208, 0.0779]                #mol  total organic carbon
totw = [0.0031, 0.0071, 0.008]           #kg   water
tots = [6.94, 2.87, 2.02]                #g    soil dry mass
ph   = [4.24, 4.86, 4.95]
cace = [5.75, 2.15, 10.76]                #mM   acetate T and P measured value
cfe2 = [22.09, 20.24, 17.45]                #mM   Fe
hdsp = [0.059, 0.059, 0.059] #head space volume L
 
index = 0
writephrq('fa', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferb, fmega, fmegh, sldoc)
 
writephrq('fa',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
		ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferb, fmega, fmegh, sldoc)

writephrq('fa',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferb, fmega, fmegh, sldoc)
 
index = 1
writephrq('ft', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferb, fmega, fmegh, sldoc)
 
writephrq('ft',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferb, fmega, fmegh, sldoc)
 
writephrq('ft',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferb, fmega, fmegh, sldoc)
 
index = 2
writephrq('fp', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbp, fmegap, fmeghp, sldoc)
 
writephrq('fp',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbp, fmegap, fmeghp, sldoc)
 
writephrq('fp',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbp, fmegap, fmeghp, sldoc)
 

