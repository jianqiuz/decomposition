import numpy as np
import math as math
from writephrq import *

fldoc   = 0.01
fsom1   = 0.1
fsom2   = 0.4
fsom3   = 0.1
fmic    = 1.0e-6

sldoc   = 0.8

ffe3    = 0.02

kfera   = 0.5
kferh   = 0.8
kmega   = 0.6
kmegh   = 0.5

kdecay  = 0.1

fsom1o  = fsom1
fsom2o  = fsom2

fsom1m  = fsom1
fsom2m  = fsom2

fsom3   = fsom3

fferbo  = fmic*10
fferbm  = fmic*10
fmeg    = fmic*4

fldoco  = fldoc 
fldocm  = fldoc
ffe3o   = ffe3
ffe3m   = ffe3


ffe3co  = ffe3o 
ffe3cm  = ffe3m
ffe3ro  = ffe3o
ffe3rm  = ffe3m
ffe3to  = ffe3o
ffe3tm  = ffe3m
fldocco = fldoco 
fldoccm = fldocm
fldocro = fldoco
fldocrm = fldocm
fldocto = fldoco
fldoctm = fldocm
fsom1co = fsom1o 
fsom1cm = fsom1m
fsom1ro = fsom1o
fsom1rm = fsom1m
fsom1to = fsom1o
fsom1tm = fsom1m
fsom2co = fsom2o
fsom2cm = fsom2m
fsom2ro = fsom2o
fsom2rm = fsom2m
fsom2to = fsom2o
fsom2tm = fsom2m
fferbco = fferbo 
fferbcm = fferbm
fferbro = fferbo
fferbrm = fferbm
fferbto = fferbo
fferbtm = fferbm
fmegaco = fmeg
fmegacm = fmeg
fmegaro = fmeg
fmegarm = fmeg
fmegato = fmeg
fmegatm = fmeg
fmegh   = fmeg
 
totc = [0.045,  0.1117, 0.104,  0.105,  0.074, 0.056]                #mol  total organic carbon
totw = [0.013588, 0.005854, 0.011788, 0.006379, 0.010690, 0.006620] #kg   water
tots = [1.41,    9.15,  3.21,   8.62,   4.31 , 8.38]                #g    soil dry mass
ph   = [5.02,    4.84,  5.21,   4.54,   5.23,  4.95]
cace = [6.370,  2.799, 0.057,  2.668,  1.026, 1.839]                #mM   acetate
cfe2 = [0.789, 22.234, 1.61, 22.973, 15.665, 7.177]                #mM   Fe
hdsp = [0.042528, 0.042528, 0.044005, 0.044005, 0.043575, 0.043575] #head space volume L
 
index = 0
writephrq('co', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3co, fldocco, fsom1co, fsom2co, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbco, fmegaco, fmegh, sldoc)
 
writephrq('co',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3co, fldocco, fsom1co, fsom2co, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbco, fmegaco, fmegh, sldoc)
 
writephrq('co',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3co, fldocco, fsom1co, fsom2co, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbco, fmegaco, fmegh, sldoc)
 
index = 1
writephrq('cm', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3cm, fldoccm, fsom1cm, fsom2cm, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbcm, fmegacm, fmegh, sldoc)
 
writephrq('cm',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3cm, fldoccm, fsom1cm, fsom2cm, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbcm, fmegacm, fmegh, sldoc)
 
writephrq('cm',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3cm, fldoccm, fsom1cm, fsom2cm, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbcm, fmegacm, fmegh, sldoc)
 
index = 2
writephrq('ro', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3ro, fldocro, fsom1ro, fsom2ro, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbro, fmegaro, fmegh, sldoc)
 
writephrq('ro',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3ro, fldocro, fsom1ro, fsom2ro, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbro, fmegaro, fmegh, sldoc)
 
writephrq('ro',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3ro, fldocro, fsom1ro, fsom2ro, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbro, fmegaro, fmegh, sldoc)
 
index = 3
writephrq('rm', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3rm, fldocrm, fsom1rm, fsom2rm, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbrm, fmegarm, fmegh, sldoc)
 
writephrq('rm',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3rm, fldocrm, fsom1rm, fsom2rm, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbrm, fmegarm, fmegh, sldoc)
 
writephrq('rm',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3rm, fldocrm, fsom1rm, fsom2rm, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbrm, fmegarm, fmegh, sldoc)
 
index = 4
writephrq('to', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3to, fldocto, fsom1to, fsom2to, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbto, fmegato, fmegh, sldoc)
 
writephrq('to',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3to, fldocto, fsom1to, fsom2to, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbto, fmegato, fmegh, sldoc)
 
writephrq('to',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3to, fldocto, fsom1to, fsom2to, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbto, fmegato, fmegh, sldoc)
 
index = 5
writephrq('tm', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3tm, fldoctm, fsom1tm, fsom2tm, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbtm, fmegatm, fmegh, sldoc)
 
writephrq('tm',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3tm, fldoctm, fsom1tm, fsom2tm, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbtm, fmegatm, fmegh, sldoc)
 
writephrq('tm',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3tm, fldoctm, fsom1tm, fsom2tm, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbtm, fmegatm, fmegh, sldoc)
 
 
