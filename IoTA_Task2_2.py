# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 21:36:09 2019

@author: JAYALAKSHMI
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:57:18 2019

@author: JAYALAKSHMI
"""
from tabulate import tabulate
from random import random
import math

IAT_RT = int(input("Enter mean inter-arival time of RT messages:"))
IAT_nRT = int(input("Enter mean inter-arival time of nonRT messages:"))
ST_RT = int(input("Enter mean service time of RT messages:"))
ST_nRT = int(input("Enter mean service time of nonRT messages:"))
mc_end = int(input("Enter the maximum value of MC:"))
mc = 0
rtcl = 3
nrtcl = 5
nrt = 0
nnrt = 0
scl = 4
s = 2
pe = 0
table = []
table.append([mc, rtcl, nrtcl, nrt, nnrt, scl, s, pe])
while mc < mc_end:
    if scl == "":
        mc = min(rtcl, nrtcl)
    else:
        mc = min(rtcl, nrtcl, scl)
    r = random()
    r_IAT_RT = -1*(IAT_RT)*math.log(r)
    r_IAT_nRT = -1*(IAT_nRT)*(math.log(r))
    r_ST_RT = -1*(ST_RT)*(math.log(r))
    r_ST_nRT = -1*(ST_nRT)*(math.log(r))
    if mc == rtcl:
        nrt = nrt + 1
        rtcl = mc + r_IAT_RT
        if nrt == 1:
            if s == 0:
                scl = mc + r_ST_RT
                nrt = nrt - 1
                s = 1
            elif s == 2:
                pe = scl - mc
                if pe != 0:
                    nnrt = nnrt + 1
                scl = mc + r_ST_RT
                nrt = nrt - 1
                s = 1
        table.append([mc, rtcl, nrtcl, nrt, nnrt, scl, s, pe])
    elif mc == nrtcl:
        nnrt = nnrt + 1
        nrtcl = mc + r_IAT_nRT
        if nnrt > 0:
            if s == 0:
                if pe > 0:
                    scl = mc + pe
                    pe = pe - (scl - mc)
                else:
                    scl = mc + r_ST_nRT
                nnrt = nnrt - 1
                s = 2
        table.append([mc, rtcl, nrtcl, nrt, nnrt, scl, s, pe])
    elif mc == scl:
        if nrt > 0:
            scl = mc + r_ST_RT
            s = 1
            nrt = nrt - 1
        elif nnrt > 0:
            if pe > 0:
                scl = mc + pe
                pe = pe - (scl - mc)
            else:
                scl = mc + r_ST_nRT
            s = 2
            nnrt = nnrt - 1
        else:
            s = 0
            scl = ""
        table.append([mc, rtcl, nrtcl, nrt, nnrt, scl, s, pe])
print(tabulate(table, headers = ["MC", "RTCL", "nRTCL", "nRT", "nNRT", "SCL", "s", "PE"]))

'''
Output table:

       MC       RTCL     nRTCL    nRT    nNRT  SCL                   s            PE
---------  ---------  --------  -----  ------  ------------------  ---  ------------
  0          3          5           0       0  4                     2   0
  3          6.35209    5           0       1  3.6704184304562615    1   1
  3.67042    6.35209    5           0       0  4.6704184304562615    2   0
  4.67042    6.35209    5           0       0                        0   0
  5          6.35209   11.0753      0       0  9.860241150908443     2   0
  6.35209    8.03738   11.0753      0       1  6.689150196641661     1   3.50815
  6.68915    8.03738   11.0753      0       0  10.197299195268796    2   0
  8.03738    8.38689   11.0753      0       1  8.10728305667057      1   2.15992
  8.10728    8.38689   11.0753      0       0  10.267199877856292    2   0
  8.38689    9.2353    11.0753      0       1  8.556568307518637     1   1.88031
  8.55657    9.2353    11.0753      0       0  10.436882398354378    2   0
  9.2353    35.6522    11.0753      0       1  14.518687270084923    1   1.20158
 11.0753    35.6522    21.1559      0       2  14.518687270084923    1   1.20158
 14.5187    35.6522    21.1559      0       1  15.720271278928323    2   0
 15.7203    35.6522    21.1559      0       0  26.78685761194378     2   0
 21.1559    35.6522    26.1047      0       1  26.78685761194378     2   0
 26.1047    35.6522    36.4771      0       2  26.78685761194378     2   0
 26.7869    35.6522    36.4771      0       1  27.579835675019773    2   0
 27.5798    35.6522    36.4771      0       0  30.570531063113705    2   0
 30.5705    35.6522    36.4771      0       0                        0   0
 35.6522    62.1995    36.4771      0       0  40.961690076163435    1   0
 36.4771    62.1995    36.6497      0       1  40.961690076163435    1   0
 36.6497    62.1995    51.7565      0       2  40.961690076163435    1   0
 40.9617    62.1995    51.7565      0       1  41.789723620743395    2   0
 41.7897    62.1995    51.7565      0       0  43.885438852221625    2   0
 43.8854    62.1995    51.7565      0       0                        0   0
 51.7565    62.1995    54.0231      0       0  53.5697470856365      2   0
 53.5697    62.1995    54.0231      0       0                        0   0
 54.0231    62.1995    57.7725      0       0  57.02257634765541     2   0
 57.0226    62.1995    57.7725      0       0                        0   0
 57.7725    62.1995    58.7357      0       0  58.54302832910905     2   0
 58.543     62.1995    58.7357      0       0                        0   0
 58.7357    62.1995    62.6799      0       0  61.8910620995337      2   0
 61.8911    62.1995    62.6799      0       0                        0   0
 62.1995    65.3837    62.6799      0       0  62.83633250200869     1   0
 62.6799    65.3837    65.6831      0       1  62.83633250200869     1   0
 62.8363    65.3837    65.6831      0       0  64.47637014126818     2   0
 64.4764    65.3837    65.6831      0       0                        0   0
 65.3837   107.342     65.6831      0       0  73.77536382632763     1   0
 65.6831   107.342     73.1076      0       1  73.77536382632763     1   0
 73.1076   107.342     77.6228      0       2  73.77536382632763     1   0
 73.7754   107.342     77.6228      0       1  75.96521159951565     2   0
 75.9652   107.342     77.6228      0       0  76.75622736344035     2   0
 76.7562   107.342     77.6228      0       0                        0   0
 77.6228   107.342     78.833       0       0  78.59099741990308     2   0
 78.591    107.342     78.833       0       0                        0   0
 78.833    107.342     81.1609      0       0  80.69532258307055     2   0
 80.6953   107.342     81.1609      0       0                        0   0
 81.1609   107.342     85.1329      0       0  84.3384909084202      2   0
 84.3385   107.342     85.1329      0       0                        0   0
 85.1329   107.342     88.5385      0       0  87.85738027697353     2   0
 87.8574   107.342     88.5385      0       0                        0   0
 88.5385   107.342     91.8702      0       0  91.20388398016306     2   0
 91.2039   107.342     91.8702      0       0                        0   0
 91.8702   107.342     92.0782      0       0  92.0366450795744      2   0
 92.0366   107.342     92.0782      0       0                        0   0
 92.0782   107.342     97.7417      0       0  96.60903650818165     2   0
 96.609    107.342     97.7417      0       0                        0   0
 97.7417   107.342     99.2469      0       0  98.94587595810829     2   0
 98.9459   107.342     99.2469      0       0                        0   0
 99.2469   107.342    100.984       0       0  100.6365212621765     2   0
100.637    107.342    100.984       0       0                        0   0
100.984    107.342    102.276       0       0  102.01780954548428    2   0
102.018    107.342    102.276       0       0                        0   0
102.276    107.342    104.838       0       0  104.32600388461728    2   0
104.326    107.342    104.838       0       0                        0   0
104.838    107.342    144.864       0       0  136.85917465680257    2   0
107.342    107.509    144.864       0       1  107.37534432449631    1  29.5173
107.375    107.509    144.864       0       0  136.89268250912454    2  -1.42109e-14
107.509    137.52     144.864       0       1  113.51142046142441    1  29.3833
113.511    137.52     144.864       0       0  142.89472723676477    2   0
137.52     166.102    144.864       0       1  143.23599890038474    1   5.37513
143.236    166.102    144.864       0       0  148.61112676516416    2   0
144.864    166.102    151.018       0       1  148.61112676516416    2   0
148.611    166.102    151.018       0       0  155.05023479593598    2   0
151.018    166.102    151.993       0       1  155.05023479593598    2   0
151.993    166.102    152.285       0       2  155.05023479593598    2   0
152.285    166.102    159.132       0       3  155.05023479593598    2   0
155.05     166.102    159.132       0       2  157.48842391526858    2   0
157.488    166.102    159.132       0       1  164.29527930962254    2   0
159.132    166.102    166.418       0       2  164.29527930962254    2   0
164.295    166.102    166.418       0       1  165.10429033494373    2   0
165.104    166.102    166.418       0       0  165.66053034477696    2   0
165.661    166.102    166.418       0       0                        0   0
166.102    175.505    166.418       0       0  167.9823023550789     1   0
166.418    175.505    169.854       0       1  167.9823023550789     1   0
167.982    175.505    169.854       0       0  172.51104524907043    2   0
169.854    175.505    171.102       0       1  172.51104524907043    2   0
171.102    175.505    172.734       0       2  172.51104524907043    2   0
172.511    175.505    172.734       0       1  177.8408817431873     2   0
172.734    175.505    173.135       0       2  177.8408817431873     2   0
173.135    175.505    192.8         0       3  177.8408817431873     2   0
175.505    199.195    192.8         0       4  180.24305131259217    1   2.33576
180.243    199.195    192.8         0       3  182.57880933631452    2   0
182.579    199.195    192.8         0       2  184.98879843226158    2   0
184.989    199.195    192.8         0       1  187.87569887026348    2   0
187.876    199.195    192.8         0       0  192.5173070162186     2   0
192.517    199.195    192.8         0       0                        0   0
192.8      199.195    199.223       0       0  197.93850347597976    2   0
197.939    199.195    199.223       0       0                        0   0
199.195    208.942    199.223       0       0  201.14429295907414    1   0
199.223    208.942    202.628       0       1  201.14429295907414    1   0
201.144    208.942    202.628       0       0  206.44823363321086    2   0

'''