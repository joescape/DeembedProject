# importing wx files
import wx
import skrf as rf
import matplotlib.pylab as plt
import numpy as np
import DeembedGUI
import DeembedFiles

class DeembedWiz(DeembedGUI.DeembedWiz):
    # constructor
    def __init__(self,parent):
        # type: (object) -> object
        # initialize parent class
        DeembedGUI.DeembedWiz.__init__(self,parent)
        
    def deembedChoiceChange(self,event):
        self.deembedchoice = self.m_deembedChoice.GetSelection()
        # print deembedchoice
        
    def tempChoiceChange(self,event):
        self.tempchoice = self.m_tempChoice.GetSelection()
        
        if self.tempchoice:
            self.m_DeembedFilePicker2.Disable()
            self.m_DeembedFilePicker3.Disable()
            self.m_DeembedFilePicker2.SetPath('')
            self.m_DeembedFilePicker3.SetPath('')
            
        else:
            self.m_DeembedFilePicker2.Enable()
            self.m_DeembedFilePicker3.Enable()

        # print tempchoice

    def Close(self,event):
        event.Skip()

    def RawDirChange(self, event):
        self.rawdir = self.m_RawDirPicker.GetPath()
        # print rawdir

    def DeembedDirChange(self, event):
        self.deembeddir = self.m_DeembedDirPicker.GetPath()
        # print deembeddir

    def DeembedFile1Change(self, event):
        self.deembedfilename1 = self.m_DeembedFilePicker1.GetPath()
        print self.deembedfilename1

    def DeembedFile2Change(self, event):
        self.deembedfilename2 = self.m_DeembedFilePicker2.GetPath()
        # print self.deembedfilename2

    def DeembedFile3Change(self, event):
        self.deembedfilename3 = self.m_DeembedFilePicker3.GetPath()
        # print self.deembedfilename3

    def startDeembed(self, event):
        DeembedFiles.deembed(self.deembedchoice,self.tempchoice,self.rawdir,self.deembeddir,self.deembedfilename1,
                             self.deembedfilename2,self.deembedfilename3)
        
# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)
 
# create an object of DeembedWiz
mywiz = DeembedWiz(None)

# configure properties of wizard
mywiz.FitToPage(mywiz.m_pages[1])
mywiz.RunWizard(mywiz.m_pages[0])
mywiz.Destroy()

# start the applications
app.MainLoop()





