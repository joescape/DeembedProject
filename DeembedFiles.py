import skrf as rf
from numpy import *
import os


def deembed(deembedtype,temps,rawpath,dpath,pcb1,pcb2,pcb3):

    pcbNet1 = rf.Network(pcb1)

    if temps == 1:
        pcbNet2 = rf.Network(pcb2)
        pcbNet3 = rf.Network(pcb3)

    # need to figure out way to only perform the open preparation once
    def allopendmbd(pcbNet,embdNet):
        pcbnetsize[] = shape(pcbNet.s)
        embdnetsize[] = shape(embdNet.s)

        idmat = identity(pcbnetsize[2])
        onesmat = ones(pcbnetsize[1],pcbnetsize[2])

        for i in xrange(1,pcbnetsize[0]):
            A = ( pcbNet.s[i,:,:]*idmat + onesmat - idmat ) / 2
            embdNet.s[i,:,:] = embdNet.s[i,:,:] / A
            B = ( pcbNet.s[i,:,:] - pcbNet.s[i,:,:]*idmat ) / 2
            embdNet.s[i,:,:] = embdNet.s[i,:,:] - B



    def oneopendmbd(pcbNet,embdNet):


    def thrudmbd(pcbNet,embdNet)


    for dirpath, dirnames, filenames in os.walk(rawpath):
        for name in filenames:
            if name.endswith('.s?p'):
                os.path.join(dirpath,name)