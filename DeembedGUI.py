# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.wizard

###########################################################################
## Class DeembedWiz
###########################################################################

class DeembedWiz ( wx.wizard.Wizard ):
	
	def __init__( self, parent ):
		wx.wizard.Wizard.__init__ ( self, parent, id = wx.ID_ANY, title = u"PSemi Deembedding Wizard", bitmap = wx.NullBitmap, pos = wx.DefaultPosition, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.DefaultSize )
		self.m_pages = []
		
		self.m_wizPage1 = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.m_wizPage1 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		m_deembedChoiceChoices = [ u"Scalar Deembedding with .sNp (All Open)", u"Scalar Deembedding with representative .s1p (Open)", u"Scalar Deembedding with representative .s2p (2x Thru)" ]
		self.m_deembedChoice = wx.RadioBox( self.m_wizPage1, wx.ID_ANY, u"Deembedding Format", wx.DefaultPosition, wx.DefaultSize, m_deembedChoiceChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_deembedChoice.SetSelection( 1 )
		self.m_deembedChoice.SetToolTipString( u"Choose Scalar De-embedding with .sNp to de-embed files with a measurement of the PCB using all ports.\n \nChoose Scalar De-embedding with representative .s1p to use a single representative trace measurement to de-embed all ports.\n\nChoose Scalar De-embedding with representative .s2p to use a 2x thru to de-embed all ports." )
		
		bSizer2.Add( self.m_deembedChoice, 1, wx.ALL|wx.EXPAND, 5 )
		
		m_tempChoiceChoices = [ u"1", u"3" ]
		self.m_tempChoice = wx.RadioBox( self.m_wizPage1, wx.ID_ANY, u"Temperatures", wx.DefaultPosition, wx.DefaultSize, m_tempChoiceChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_tempChoice.SetSelection( 0 )
		self.m_tempChoice.SetToolTipString( u"Choose 1 to de-embed files with 1 representative open or 2x thru file and 3 to de-embed files with 3 different representative files (1 for each temperature). Using 1 file, the filename of the PCB representative file will be ignored. Using 3 files, the filename of the representative file should be a subset of the filename of the embedded S-parameter file e.g. '90C.snp' to de-embed 'PEXXXXXX_1p8V_90C.snp'" )
		
		bSizer2.Add( self.m_tempChoice, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_RawDirLabel = wx.StaticText( self.m_wizPage1, wx.ID_ANY, u"Raw Data Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_RawDirLabel.Wrap( -1 )
		bSizer2.Add( self.m_RawDirLabel, 1, wx.EXPAND|wx.ALL, 5 )
		
		self.m_RawDirPicker = wx.DirPickerCtrl( self.m_wizPage1, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.m_RawDirPicker.SetToolTipString( u"Select folder location of embedded S-parameter files" )
		
		bSizer2.Add( self.m_RawDirPicker, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_DeembedDirLabel = wx.StaticText( self.m_wizPage1, wx.ID_ANY, u"De-embedded Data Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_DeembedDirLabel.Wrap( -1 )
		bSizer2.Add( self.m_DeembedDirLabel, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_DeembedDirPicker = wx.DirPickerCtrl( self.m_wizPage1, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.m_DeembedDirPicker.SetToolTipString( u"Select folder location to save de-embedded S-parameter files" )
		
		bSizer2.Add( self.m_DeembedDirPicker, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_DeembedFileLabel = wx.StaticText( self.m_wizPage1, wx.ID_ANY, u"De-embed File (.sNp)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_DeembedFileLabel.Wrap( -1 )
		self.m_DeembedFileLabel.SetToolTipString( u"Ensure that files used to de-embed are named with the temperature that they represent in any particular order" )
		
		bSizer2.Add( self.m_DeembedFileLabel, 0, wx.ALL, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.AddGrowableCol( 1 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_Temp1Label = wx.StaticText( self.m_wizPage1, wx.ID_ANY, u"Temperature 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Temp1Label.Wrap( -1 )
		fgSizer3.Add( self.m_Temp1Label, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_DeembedFilePicker1 = wx.FilePickerCtrl( self.m_wizPage1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_DeembedFilePicker1.SetToolTipString( u"Select 1st open or 2x thru S-parameter file. Ensure filename is consistent with temperature e.g. '25C.snp' or 'AMB.snp'" )
		
		fgSizer3.Add( self.m_DeembedFilePicker1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_Temp2Label = wx.StaticText( self.m_wizPage1, wx.ID_ANY, u"Temperature 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Temp2Label.Wrap( -1 )
		fgSizer3.Add( self.m_Temp2Label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_DeembedFilePicker2 = wx.FilePickerCtrl( self.m_wizPage1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_DeembedFilePicker2.SetToolTipString( u"Select 2nd open or 2x thru S-parameter file. Ensure filename is consistent with temperature e.g. 'N40C.snp'" )
		
		fgSizer3.Add( self.m_DeembedFilePicker2, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_Temp3Label = wx.StaticText( self.m_wizPage1, wx.ID_ANY, u"Temperature 3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Temp3Label.Wrap( -1 )
		fgSizer3.Add( self.m_Temp3Label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_DeembedFilePicker3 = wx.FilePickerCtrl( self.m_wizPage1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_DeembedFilePicker3.SetToolTipString( u"Select 3rd open or 2x thru S-parameter file. Ensure filename is consistent with temperature e.g. '90C.snp'" )
		
		fgSizer3.Add( self.m_DeembedFilePicker3, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer2.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		self.m_wizPage1.SetSizer( bSizer2 )
		self.m_wizPage1.Layout()
		bSizer2.Fit( self.m_wizPage1 )
		self.m_wizPage2 = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.m_wizPage2 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_SmithChartIcon = wx.StaticBitmap( self.m_wizPage2, wx.ID_ANY, wx.Bitmap( u"300px-Smith_chart_gen.svg.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_SmithChartIcon.SetToolTipString( u"Learn the Smith Chart... master the RF domain!" )
		
		bSizer10.Add( self.m_SmithChartIcon, 0, wx.ALL|wx.EXPAND, 5 )
		
		gbSizer1 = wx.GridBagSizer( 0, 10 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_OpenRawcheckBox = wx.CheckBox( self.m_wizPage2, wx.ID_ANY, u"Open Raw Data Directory After Completion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_OpenRawcheckBox.SetToolTipString( u"Select this option in order to open the raw data directory after de-embedding" )
		
		gbSizer1.Add( self.m_OpenRawcheckBox, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )
		
		self.m_OpenDeembeddedcheckBox = wx.CheckBox( self.m_wizPage2, wx.ID_ANY, u"Open De-embedded Data Directory After Completion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_OpenDeembeddedcheckBox.SetToolTipString( u"Select this option in order to open the de-embedded data directory after de-embedding" )
		
		gbSizer1.Add( self.m_OpenDeembeddedcheckBox, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )
		
		self.m_DeembedButton = wx.Button( self.m_wizPage2, wx.ID_ANY, u"De-embed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_DeembedButton.SetToolTipString( u"Start de-embedding" )
		
		gbSizer1.Add( self.m_DeembedButton, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer10.Add( gbSizer1, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_ProgressGauge = wx.Gauge( self.m_wizPage2, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_ProgressGauge.SetValue( 0 ) 
		bSizer10.Add( self.m_ProgressGauge, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_ProgressText = wx.StaticText( self.m_wizPage2, wx.ID_ANY, u"0 of 21 files completed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ProgressText.Wrap( -1 )
		bSizer10.Add( self.m_ProgressText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_wizPage2.SetSizer( bSizer10 )
		self.m_wizPage2.Layout()
		bSizer10.Fit( self.m_wizPage2 )
		self.Centre( wx.BOTH )
		
		
		# Connect Events
		self.Bind( wx.wizard.EVT_WIZARD_CANCEL, self.Close )
		self.Bind( wx.wizard.EVT_WIZARD_FINISHED, self.Close )
		self.m_deembedChoice.Bind( wx.EVT_RADIOBOX, self.deembedChoiceChange )
		self.m_tempChoice.Bind( wx.EVT_RADIOBOX, self.tempChoiceChange )
		self.m_RawDirPicker.Bind( wx.EVT_DIRPICKER_CHANGED, self.RawDirChange )
		self.m_DeembedDirPicker.Bind( wx.EVT_DIRPICKER_CHANGED, self.DeembedDirChange )
		self.m_DeembedFilePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.DeembedFile1Change )
		self.m_DeembedFilePicker2.Bind( wx.EVT_FILEPICKER_CHANGED, self.DeembedFile2Change )
		self.m_DeembedFilePicker3.Bind( wx.EVT_FILEPICKER_CHANGED, self.DeembedFile3Change )
		self.m_OpenRawcheckBox.Bind( wx.EVT_CHECKBOX, self.openRawChoice )
		self.m_OpenDeembeddedcheckBox.Bind( wx.EVT_CHECKBOX, self.OpenDeembedChoice )
		self.m_DeembedButton.Bind( wx.EVT_BUTTON, self.startDeembed )
	def add_page(self, page):
		if self.m_pages:
			previous_page = self.m_pages[-1]
			page.SetPrev(previous_page)
			previous_page.SetNext(page)
		self.m_pages.append(page)
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Close( self, event ):
		event.Skip()
	
	
	def deembedChoiceChange( self, event ):
		event.Skip()
	
	def tempChoiceChange( self, event ):
		event.Skip()
	
	def RawDirChange( self, event ):
		event.Skip()
	
	def DeembedDirChange( self, event ):
		event.Skip()
	
	def DeembedFile1Change( self, event ):
		event.Skip()
	
	def DeembedFile2Change( self, event ):
		event.Skip()
	
	def DeembedFile3Change( self, event ):
		event.Skip()
	
	def openRawChoice( self, event ):
		event.Skip()
	
	def OpenDeembedChoice( self, event ):
		event.Skip()
	
	def startDeembed( self, event ):
		event.Skip()
	

