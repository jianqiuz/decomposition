import numpy as np
import math as math
from writephrq import *

def writephrq(prefix, temperature, \
              totc, totw, tots, headspace, ph, cace, fe2, ffe3, \
              fldoc, fsom1, fsom2, fsom3, \
              kfera, kferh, kmega, kmegh, kdecay, \
              fferb, fmega, fmegh, dldoc):  

  name  = prefix + '%1d'%(abs(temperature))
  fname = name + '.phrq'
  ofile = open(fname, 'w')
  molecular_weight_c = 12.0107
  molecular_weight_feoh3 = 106.867

  tmf = math.exp(308.56*(1.0/71.02-1.0/(273.15 + temperature - 227.13)))
#Ratkowsky
#TK = temperature + 273.15
#3T0 = 298.15
#Tm = 265.00
#tmf = (TK - Tm) * (TK - Tm) / (T0 - Tm) / (T0 - Tm)


  prefix_solution = """
DATABASE ../database/redox.dat

TITLE simulate CO2 and CH4 production from microcosm tests

CALCULATE_VALUES
 fpH
 -start
 10 pH = -la("H+")
 20 if pH < 7.0 then fpH = 1.02 / (1.0 + 1.0e6 * exp(-2.5 * pH))
 30 if pH > 7.0 then fpH = 1.02 / (1.0 + 1.0e6 * exp(-2.5 * (14.0 - pH)))
 40 if pH < 4.0 then fpH = 0.0
 50 if pH > 10.0 then fpH = 0.0
 60 SAVE fpH
 -end

SOLUTION 1
  units       mmol/kgw
"""

  ofile.write(prefix_solution)

  ofile.write('  temperature \t %3.1f\n'%(temperature))
  ofile.write('  pH \t %4.2f\n'%(ph))
  ofile.write('  water \t %10.6f\n'%(totw))
  ofile.write('  Acetate \t %10.2f\n'%(cace))

  cglucose = totc * 1000.0 * fldoc / totw / 6.0
  ofile.write('  Glucose \t %10.2f\n'%(cglucose))

  ofile.write('  Ferrous \t %10.2f\n'%(fe2))

  postfix_solution = """
  C(4)        1.0 redoxCO2(g) -3.4  # in equilibrium with CO2 in atmosphere, 400 pm
  Ca          1.0
  Na          1.0
  Cl          1.0 charge
  Hzero       1.0e-10
  Nzero       1.0 redoxN2(g) 0.0
  Ferric      1e-20 redoxFe(OH)3(a) 0.0
  Methane     1.0e-10
  Amm         1.0e-3
  SAVE SOLUTION 1
END

"""

  ofile.write(postfix_solution)

  prefix_gasphase = """
GAS_PHASE 1 fixed volume gas phase
  -fixed_volume
"""

  ofile.write(prefix_gasphase)

  ofile.write('  -volume \t %10.6f\n'%(headspace))
  ofile.write('  temperature \t %3.1f\n'%(temperature))

  postfix_gasphase = """
  redoxCH4(g) 0.0
  redoxCO2(g) 0.0
  redoxH2(g)  0.0
  redoxN2(g)  1.0
  redoxNH3(g) 0.0
  SAVE GAS_PHASE 1
END
"""
 
  ofile.write(postfix_gasphase)

  prefix_phase = """ 
USE SOLUTION 1
USE GAS_PHASE 1
 
EQUILIBRIUM_PHASES 1
"""

  ofile.write(prefix_phase)

  cfe3 = ffe3 * tots / molecular_weight_feoh3   # Fe(OH)3 mw 106.867 
  ofile.write('  redoxFe(OH)3(a) 0.0 %12.8E\n'%(cfe3))

  ofile.write('SURFACE 1\n')

  ofile.write('Hfo_w redoxFe(OH)3(a) 0.2 1.068E4\n')
  ofile.write('Hfo_s redoxFe(OH)3(a) 0.005 1.068E4\n')

  om_gram = totc * molecular_weight_c
  surf    = 34.17e3
  ha      = om_gram * 7.10E-04*1
  hb      = om_gram * 3.55E-04*1
  hc      = om_gram * 1.18E-04*1

  ofile.write('  H_a  %10.3E %10.3E %10.3f\n'%(ha, surf, om_gram))
  ofile.write('  H_b  %10.3E; H_c  %10.3E; H_d %10.3E\n'%(ha, ha, ha))
  ofile.write('  H_e  %10.3E; H_f  %10.3E; H_g %10.3E; H_h %10.3E\n'%(hb, hb, hb, hb))
  ofile.write('  H_ab %10.3E; H_ad %10.3E; H_af %10.3E; H_ah %10.3E\n'%(hc, hc, hc, hc))
  ofile.write('  H_bc %10.3E; H_be %10.3E; H_bg %10.3E; H_cd %10.3E\n'%(hc, hc, hc, hc))
  ofile.write('  H_cf %10.3E; H_ch %10.3E; H_de %10.3E; H_dg %10.3E\n'%(hc, hc, hc, hc))
  ofile.write('  -equil 1\n')

  ofile.write('KINETICS\n')
  ofile.write('  -cvode\n')

  ofile.write('  FeRAk\n')
  ofile.write('    -formula Ferrous -150.1676 H -166.4385 HCO3 -37.5419 Ferric 150.1676 H2O 72.0838 Acetate 21.2709\n')
  kferak = kfera / 86400.0 #8.68e-5  # 0.75 d-1 0.014 h-1 Holmes et al. 2013, 0.04-0.09 h-1 Esteve-Nunez et al 2005; 0.088, 0.023 h-1 Cord-Ruwisch 1998 
  ofile.write('    -parms  %10.3E 1.2E-5 0.062 1.0E-6\n\n'%(kferak*tmf))
  
  kferhk = kferh / 86400.0 #1.16e-6  # 1 d-1
  ofile.write('  FeRHk\n')
  ofile.write('    -formula Ferrous -114.7648 H -109.7648 H2O -13.0 Ferric 114.7648 HCO3 5.0 Hzero2 67.3824\n')
  ofile.write('    -parms  %10.3E 1.0E-6 0.062 1.0E-6\n\n'%(kferhk*tmf))

  kdecay = kdecay/86400.0 #5.787e-7 # Rittman and McCarty 2001 0.05 d-1
  ofile.write('  FeRd\n')
  ofile.write('    -m0 %10.3E\n\n'%(fferb*totc/5.0))
  ofile.write('    -formula CH2O 0.0\n')
  ofile.write('    -parms %10.3E\n\n'%(tmf*kdecay*10))

  ofile.write('  FeRb\n')
  ofile.write('    -formula CH2O 0.0\n')
  ofile.write('    -m0 %10.3E\n\n'%(fferb*totc/5.0))

  ofile.write('  MeGAk\n')
  kmegak = kmega/86400.0 #3.470e-6    # 0.3 1/d Rittmann and McCarty 2001 p169 table 3.1
  ofile.write('    -formula HCO3 -101.1836 MethaneH4 -101.1836 H 1.5 H2O 98.1836 Acetate 103.6836\n')
  ofile.write('    -parms %10.3E 2.3e-5 1.0e-6\n\n'%(tmf*kmegak))

  ofile.write('  MeGAd\n')
  ofile.write('    -m0 %10.3E\n\n'%(fmega*totc/5.0))
  ofile.write('    -formula CH2O 0.0\n')
  ofile.write('    -parms %10.3E\n\n'%(tmf*kdecay*10))

  ofile.write('  MeGAb\n')
  ofile.write('    -formula CH2O 0.0\n')
  ofile.write('    -m0 %10.3E\n\n'%(fmega*totc/5.0))

  ofile.write('  MeGHk\n')
  kmeghk = kmegh/86400.0 #5.79e-6    # 0.5 1/d Rittmann and McCarty 2001 p169 table 3.1
  ofile.write('    -formula H2O -255.6428 MethaneH4 -80.8809 H 84.8809 Hzero2 333.5237 HCO3 85.8809\n')
  ofile.write('    -parms %10.3E 4.7e-6 1.0e-6\n\n'%(tmf*kmeghk))

  ofile.write('  MeGHd\n')
  ofile.write('    -m0 %10.3E\n\n'%(0))
  ofile.write('    -formula CH2O 0.0\n')
  ofile.write('    -parms %10.3E\n\n'%(tmf*kdecay*10))

  ofile.write('  MeGHb\n')
  ofile.write('    -formula CH2O 0.0\n')
  ofile.write('    -m0 %10.3E\n\n'%(fmegh*totc/5.0))

  #labile metabolic decomposition rate 20 h, Rittmann and McCarty 2001 p169 table 3.1 1.2 d-1
  ofile.write('  Fermentation\n')
  ofile.write('    -formula Glucose 1.0 H2O 4.0 Acetate -2.0 HCO3 -2.0 H -4.0 Hzero2 -4.0\n')
  ofile.write('    -parms %10.3E\n\n'%(tmf * 0.5e-8))

  ofile.write('  SOM1\n')
  ofile.write('    -m0 %10.3E\n'%(fsom1*totc))
  ofile.write('    -formula CH2O 0.0\n')
  ofile.write('    -parms %10.3E 0.10\n\n'%(tmf * 8.399e-7))

  ofile.write('  SOM2\n')
  ofile.write('    -m0 %10.3E\n'%(fsom2*totc))
  ofile.write('    -formula CH2O 0.0\n')
  ofile.write('    -parms %10.3E 0.15\n\n'%(tmf * 1.632e-7))

  ofile.write('  SOM3\n')
  ofile.write('    -m0 %10.3E\n'%(fsom3*totc))
  ofile.write('    -formula CH2O 0.0\n')
  ofile.write('    -parms %10.3E 0.20\n\n'%(tmf * 1.622e-8))

  ofile.write('  SOM4\n')
  ofile.write('    -m0 %10.3E\n'%((1.0 - fsom1 - fsom2 - fsom3 - fldoc)*totc))
  ofile.write('    -formula CH2O 0.0\n')
  ofile.write('    -parms %10.3E 0.45\n\n'%(tmf * 1.157e-9))

  ofile.write('  Respiration\n')
  ofile.write('    -formula CO2 %5.3f Glucose %5.3f\n\n'%(-(1.0 - dldoc), -dldoc/6.0))

  ofile.write('  -steps 8e6 in 8000 steps\n')
 
  ofile.write('INCREMENTAL_REACTIONS true\n')

  ofile.write('PRINT\n') 
  ofile.write('  -reset false\n')

  ofile.write('SELECTED_OUTPUT\n')
  ofile.write('  -RESET false\n')
  ofile.write('  -FILE ' + name + '.txt')

  output = """
USER_PUNCH
  -start
  -heading Time(d) pH Ac Glucose Fulvic WEOC Fe(2) Fe(3) CO2(gmole) CH4(gmole) H2(gmole) CO2s(mole) Fe(OH)3a SOM1 SOM2 SOM3 SOM4 FeRb MeGAb MeGHb Ac- Fe+2 Fe+3 H2 fpH
  10 PUNCH SIM_TIME / 86400.0
  20 PUNCH -la("H+")
  30 PUNCH tot('Acetate')*1000.0 tot('Glucose')*1000.0, tot('Fulvic')*1000.0 (tot('Acetate')*2.0+tot('Glucose')*6.0+tot('Fulvic'))*1000.0
  40 PUNCH tot('Ferrous')*1000.0 tot('Ferric')*1000.0
  50 PUNCH GAS('redoxCO2(g)')*1000000 GAS('redoxCH4(g)')*1000000 GAS('redoxH2(g)')*1000000
  60 PUNCH surf("C(4)", "Hfo")
"""

  ofile.write(output)

  ofile.write(' 100 PUNCH equi(\'redoxFe(OH)3(a)\')/%10.6f*1000.0\n'%(totw))
  ofile.write(' 110 PUNCH kin(\'SOM1\') kin(\'SOM2\') kin(\'SOM3\') kin(\'SOM4\')\n')
  ofile.write(' 120 PUNCH kin(\'FeRb\') kin(\'MeGAb\') kin(\'MeGHb\')\n')
  ofile.write(' 130 PUNCH mol(\'Acetate-\')*1000.0 mol(\'Ferrous+2\')*1000.0 mol(\'Ferric+3\')*1000.0 mol(\'Hzero2\')*1000.0\n')
  ofile.write(' 140 PUNCH CALC_VALUE(\'fpH\')\n')

  output = """
  -end
END
"""
  ofile.write(output)

  ofile.close()


