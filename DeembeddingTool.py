#importing wx files
import os
import wx
import skrf as rf
import matplotlib.pylab as plt
import numpy as np
 
#import the newly created GUI file
import DeembedGUI
 
#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class DeembedWiz(DeembedGUI.DeembedWiz):
    #constructor
    def __init__(self,parent):
        # type: (object) -> object
        #initialize parent class
        DeembedGUI.DeembedWiz.__init__(self,parent)
        
    def deembedChoiceChange(self,event):
        deembedChoice = self.m_deembedChoice.GetSelection()
        
    def tempChoiceChange(self,event):
        tempChoice = self.m_tempChoice.GetSelection()
        
        if tempChoice:
            self.m_DeembedFilePicker2.Disable()
            self.m_DeembedFilePicker3.Disable()
            self.m_DeembedFilePicker2.SetPath('')
            self.m_DeembedFilePicker3.SetPath('')
            
        else:
            self.m_DeembedFilePicker2.Enable()
            self.m_DeembedFilePicker3.Enable()
    
    def Close(self,event):
        event.Skip()

    def RawDirChange(self, event):
        RawDir = self.m_RawDirPicker.GetPath()
        for root, dirs, files in os.walk(RawDir):
            print root

    def DeembedDirChange(self, event):
        DeembedDir = self.m_DeembedDirPicker.GetPath()

    def DeembedFile1Change(self, event):
        DeembedFilename1 = self.m_DeembedFilePicker1.GetPath()

    def DeembedFile2Change(self, event):
        DeembedFilename2 = self.m_DeembedFilePicker2.GetPath()

    def DeembedFile3Change(self, event):
        DeembedFilename3 = self.m_DeembedFilePicker3.GetPath()
        
        
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



#
#touchstone_file1 = os.path.join('C:\\Users\\jslaton\\Desktop\\PythonDeembedProject','DIE73.s3p')
#touchstone_file2 = os.path.join('C:\\Users\\jslaton\\Desktop\\PythonDeembedProject','OPEN.s3p')
#
#OPEN = rf.Network(touchstone_file2)
#DIE73 = rf.Network(touchstone_file1)
#
#DIE73Path1 = rf.Network(frequency = DIE73.f, s=DIE73.s[:,:2,:2])
#OPENPath1 = rf.Network(frequency = OPEN.f, s=OPEN.s[:,:2,:2])
#
#denom_s21 = np.sqrt(OPENPath1.s[:,0,0]) * np.sqrt(OPENPath1.s[:,1,1])
#numer_s21 = DIE73Path1.s[:,0,1] - OPENPath1.s[:,0,1]
#s21 = np.divide(numer_s21,denom_s21)
#s11 = np.divide(DIE73.s[:,0,0],OPEN.s[:,0,0])
#s_deembedded = np.array([[s11, s21],[s21,s11]])
##s_deembedded = s_deembedded.
#
#deembedded = rf.Network(f=DIE73.f, s = s_deembedded)
#
#rf.stylely()
#fig = plt.figure()
#DIE73.s21.plot_s_db()
##OPEN.s21.plot_s_db()
##deembedded.s21.plot_s_db()
##DIE73Path1.plot_s_db()
##deembedded.plot_s_db()