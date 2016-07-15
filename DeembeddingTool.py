#importing wx files
import os
import wx
import skrf as rf
import matplotlib.pylab as plt
import numpy as np
 
#import the GUI file
import DeembedGUI

class DeembedWiz(DeembedGUI.DeembedWiz):
    #constructor
    def __init__(self,parent):
        # type: (object) -> object
        #initialize parent class
        DeembedGUI.DeembedWiz.__init__(self,parent)
        
    def deembedChoiceChange(self,event):
        deembedchoice = self.m_deembedChoice.GetSelection()
        #print deembedchoice
        
    def tempChoiceChange(self,event):
        tempchoice = self.m_tempChoice.GetSelection()
        
        if tempchoice:
            self.m_DeembedFilePicker2.Disable()
            self.m_DeembedFilePicker3.Disable()
            self.m_DeembedFilePicker2.SetPath('')
            self.m_DeembedFilePicker3.SetPath('')
            
        else:
            self.m_DeembedFilePicker2.Enable()
            self.m_DeembedFilePicker3.Enable()

        #print tempchoice

    def Close(self,event):
        event.Skip()

    def RawDirChange(self, event):
        rawdir = self.m_RawDirPicker.GetPath()
        #print rawdir

    def DeembedDirChange(self, event):
        deembeddir = self.m_DeembedDirPicker.GetPath()
        #print deembeddir

    def DeembedFile1Change(self, event):
        deembedfilename1 = self.m_DeembedFilePicker1.GetPath()
        #print deembedfilename1

    def DeembedFile2Change(self, event):
        deembedfilename2 = self.m_DeembedFilePicker2.GetPath()
        #print deembedfilename2

    def DeembedFile3Change(self, event):
        deembedfilename3 = self.m_DeembedFilePicker3.GetPath()
        #print deembedfilename3
        
#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)
 
#create an object of DeembedWiz
mywiz = DeembedWiz(None)

#configure properties of wizard
mywiz.FitToPage(mywiz.m_pages[1])
mywiz.RunWizard(mywiz.m_pages[0])
mywiz.Destroy()

#start the applications
app.MainLoop()





