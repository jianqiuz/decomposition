import numpy as np
import math as math
from writephrq import *

fldoc   = 0.01
fsom1   = 0.01
fsom2   = 0.02
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


fferb  = fmic*0.5
fmega    = fmic*3
fmegh  = fmega

fferbp  = fmicp*2
fmegap    = fmicp*0.5
fmeghp  = fmegap
 
totc = [0.1465, 0.0164]                #mol  total organic carbon
totw = [0.0052, 0.0028]           #kg   water
tots = [4.76,7.19]                #g    soil dry mass
ph   = [5.92, 7.06]
cace = [0.47, 4.05]                #mM   acetate T and P measured value
cfe2 = [2.67,4.99]                #mM   Fe
hdsp = [0.059, 0.059] #head space volume L
 
##NGADG0073 mineral and permafrost

index = 0
writephrq('pm', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferb, fmega, fmegh, sldoc)
 
writephrq('pm',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferb, fmega, fmegh, sldoc)
 
writephrq('pm',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferb, fmega, fmegh, sldoc)
 
index = 1
writephrq('pf', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbp, fmegap, fmeghp, sldoc)
 
writephrq('pf',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbp, fmegap, fmeghp, sldoc)
 
writephrq('pf',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3, fldoc, fsom1, fsom2, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbp, fmegap, fmeghp, sldoc)
 

