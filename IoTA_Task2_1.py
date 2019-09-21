# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:57:18 2019

@author: JAYALAKSHMI
"""
from tabulate import tabulate

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
    if mc == rtcl:
        nrt = nrt + 1
        rtcl = mc + IAT_RT
        if nrt == 1:
            if s == 0:
                scl = mc + ST_RT
                nrt = nrt - 1
                s = 1
            elif s == 2:
                pe = scl - mc
                if pe != 0:
                    nnrt = nnrt + 1
                scl = mc + ST_RT
                nrt = nrt - 1
                s = 1
        table.append([mc, rtcl, nrtcl, nrt, nnrt, scl, s, pe])
    elif mc == nrtcl:
        nnrt = nnrt + 1
        nrtcl = mc + IAT_nRT
        if nnrt > 0:
            if s == 0:
                if pe > 0:
                    scl = mc + pe
                    pe = pe - (scl - mc)
                else:
                    scl = mc + ST_nRT
                nnrt = nnrt - 1
                s = 2
        table.append([mc, rtcl, nrtcl, nrt, nnrt, scl, s, pe])
    elif mc == scl:
        if nrt != 0:
            scl = mc + ST_RT
            s = 1
            nrt = nrt - 1
        elif nnrt != 0:
            if pe > 0:
                scl = mc + pe
                pe = pe - (scl - mc)
            else:
                scl = mc + ST_nRT
            s = 2
            nnrt = nnrt - 1
        else:
            s = 0
            scl = ""
        table.append([mc, rtcl, nrtcl, nrt, nnrt, scl, s, pe])
print(tabulate(table, headers = ["MC", "RTCL", "nRTCL", "nRT", "nNRT", "SCL", "s", "PE"]))

'''
Output 1.2:

  MC    RTCL    nRTCL    nRT    nNRT    SCL    s    PE
----  ------  -------  -----  ------  -----  ---  ----
   0       3        5      0       0      4    2     0
   3      13        5      0       1      5    1     1
   5      13       10      0       2      5    1     1
   5      13       10      0       1      6    2     0
   6      13       10      0       0     10    2     0
  10      13       15      0       1     10    2     0
  10      13       15      0       0     14    2     0
  13      23       15      0       1     15    1     1
  15      23       20      0       2     15    1     1
  15      23       20      0       1     16    2     0
  16      23       20      0       0     20    2     0
  20      23       25      0       1     20    2     0
  20      23       25      0       0     24    2     0
  23      33       25      0       1     25    1     1
  25      33       30      0       2     25    1     1
  25      33       30      0       1     26    2     0
  26      33       30      0       0     30    2     0
  30      33       35      0       1     30    2     0
  30      33       35      0       0     34    2     0
  33      43       35      0       1     35    1     1
  35      43       40      0       2     35    1     1
  35      43       40      0       1     36    2     0
  36      43       40      0       0     40    2     0
  40      43       45      0       1     40    2     0
  40      43       45      0       0     44    2     0
  43      53       45      0       1     45    1     1
  45      53       50      0       2     45    1     1
  45      53       50      0       1     46    2     0
  46      53       50      0       0     50    2     0
  50      53       55      0       1     50    2     0


Output 1.2:

  MC    RTCL    nRTCL    nRT    nNRT    SCL    s    PE
----  ------  -------  -----  ------  -----  ---  ----
   0       3        5      0       0      4    2     0
   3       8        5      0       1      7    1     1
   5       8       15      0       2      7    1     1
   7       8       15      0       1      8    2     0
   8      13       15      0       1     12    1     0
  12      13       15      0       0     14    2     0
  13      18       15      0       1     17    1     1
  15      18       25      0       2     17    1     1
  17      18       25      0       1     18    2     0
  18      23       25      0       1     22    1     0
  22      23       25      0       0     24    2     0
'''
