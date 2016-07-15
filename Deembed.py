# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import skrf as rf
import os
import matplotlib.pylab as plt
import numpy as np

touchstone_file1 = os.path.join('C:\\Users\\jslaton\\Desktop\\PythonDeembedProject','DIE73.s3p')
touchstone_file2 = os.path.join('C:\\Users\\jslaton\\Desktop\\PythonDeembedProject','OPEN.s3p')

OPEN = rf.Network(touchstone_file2)
DIE73 = rf.Network(touchstone_file1)

DIE73Path1 = rf.Network(frequency = DIE73.f, s=DIE73.s[:,:2,:2])
OPENPath1 = rf.Network(frequency = OPEN.f, s=OPEN.s[:,:2,:2])

denom_s21 = np.sqrt(OPENPath1.s[:,0,0]) * np.sqrt(OPENPath1.s[:,1,1])
numer_s21 = DIE73Path1.s[:,0,1] - OPENPath1.s[:,0,1]
s21 = np.divide(numer_s21,denom_s21)
s11 = np.divide(DIE73.s[:,0,0],OPEN.s[:,0,0])
s_deembedded = np.array([[s11, s21],[s21,s11]])
#s_deembedded = s_deembedded.

deembedded = rf.Network(f=DIE73.f, s = s_deembedded)

rf.stylely()
fig = plt.figure()
DIE73.s21.plot_s_db()
#OPEN.s21.plot_s_db()
#deembedded.s21.plot_s_db()
#DIE73Path1.plot_s_db()
#deembedded.plot_s_db()


