# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class AppFrame
###########################################################################

class AppFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"reNamer", pos = wx.DefaultPosition, size = wx.Size( 640,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.AddGrowableRow( 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_directoryCtl = wx.GenericDirCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.DIRCTRL_3D_INTERNAL|wx.DIRCTRL_DIR_ONLY|wx.SUNKEN_BORDER, wx.EmptyString, 0 )
		
		self.m_directoryCtl.ShowHidden( False )
		self.m_directoryCtl.SetMaxSize( wx.Size( 200,-1 ) )
		
		fgSizer1.Add( self.m_directoryCtl, 1, wx.ALL|wx.EXPAND, 5 )
		
		rightSectionSizer = wx.FlexGridSizer( 3, 1, 0, 8 )
		rightSectionSizer.AddGrowableCol( 0 )
		rightSectionSizer.AddGrowableRow( 1 )
		rightSectionSizer.SetFlexibleDirection( wx.BOTH )
		rightSectionSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		rightSectionSizer.SetMinSize( wx.Size( 120,80 ) ) 
		regexGroupSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Regex" ), wx.HORIZONTAL )
		
		regexFlexSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		regexFlexSizer.AddGrowableCol( 1 )
		regexFlexSizer.SetFlexibleDirection( wx.HORIZONTAL )
		regexFlexSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.reFromText = wx.StaticText( regexGroupSizer.GetStaticBox(), wx.ID_ANY, u"From", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.reFromText.Wrap( -1 )
		regexFlexSizer.Add( self.reFromText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT, 5 )
		
		self.m_reFromCtl = wx.TextCtrl( regexGroupSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PROCESS_ENTER )
		self.m_reFromCtl.SetToolTipString( u"Enter the regular expression you want to match on." )
		self.m_reFromCtl.SetMinSize( wx.Size( 200,-1 ) )
		self.m_reFromCtl.SetMaxSize( wx.Size( 200,-1 ) )
		
		regexFlexSizer.Add( self.m_reFromCtl, 1, wx.ALIGN_LEFT|wx.EXPAND|wx.FIXED_MINSIZE|wx.RIGHT, 5 )
		
		self.reToText = wx.StaticText( regexGroupSizer.GetStaticBox(), wx.ID_ANY, u"To", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.reToText.Wrap( -1 )
		regexFlexSizer.Add( self.reToText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT, 5 )
		
		self.m_reToCtl = wx.TextCtrl( regexGroupSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PROCESS_ENTER )
		self.m_reToCtl.SetToolTipString( u"Enter the substitutation pattern you want for matched files" )
		self.m_reToCtl.SetMinSize( wx.Size( 200,-1 ) )
		self.m_reToCtl.SetMaxSize( wx.Size( 200,-1 ) )
		
		regexFlexSizer.Add( self.m_reToCtl, 1, wx.ALIGN_LEFT|wx.ALIGN_RIGHT|wx.EXPAND|wx.FIXED_MINSIZE|wx.RIGHT, 5 )
		
		
		regexGroupSizer.Add( regexFlexSizer, 2, wx.ALIGN_LEFT|wx.ALIGN_RIGHT|wx.ALIGN_TOP|wx.EXPAND, 5 )
		
		
		rightSectionSizer.Add( regexGroupSizer, 2, wx.ALIGN_TOP|wx.EXPAND|wx.LEFT, 5 )
		
		listSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Files" ), wx.HORIZONTAL )
		
		m_fileListChoices = []
		self.m_fileList = wx.ListBox( listSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,120 ), m_fileListChoices, wx.LB_NEEDED_SB )
		self.m_fileList.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_fileList.SetMinSize( wx.Size( 200,120 ) )
		
		listSizer.Add( self.m_fileList, 2, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )
		
		
		rightSectionSizer.Add( listSizer, 2, wx.EXPAND|wx.LEFT, 5 )
		
		applSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_applyBtn = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_applyBtn.Enable( False )
		
		applSizer.Add( self.m_applyBtn, 0, wx.ALIGN_RIGHT|wx.BOTTOM, 4 )
		
		
		rightSectionSizer.Add( applSizer, 0, wx.ALIGN_RIGHT|wx.RIGHT, 10 )
		
		
		fgSizer1.Add( rightSectionSizer, 2, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_directoryCtl.Bind( wx.EVT_TREE_SEL_CHANGED, self.onDirectorySelectionChanged )
		self.m_reFromCtl.Bind( wx.EVT_KILL_FOCUS, self.onUnfocusRegex )
		self.m_reFromCtl.Bind( wx.EVT_SET_FOCUS, self.onFocusRegex )
		self.m_reFromCtl.Bind( wx.EVT_TEXT, self.onTextChange )
		self.m_reFromCtl.Bind( wx.EVT_TEXT_ENTER, self.onHitEnterInFrom )
		self.m_reToCtl.Bind( wx.EVT_KILL_FOCUS, self.onUnfocusRegex )
		self.m_reToCtl.Bind( wx.EVT_SET_FOCUS, self.onFocusRegex )
		self.m_reToCtl.Bind( wx.EVT_TEXT, self.onTextChange )
		self.m_reToCtl.Bind( wx.EVT_TEXT_ENTER, self.onHitEnterInTo )
		self.m_applyBtn.Bind( wx.EVT_LEFT_DOWN, self.onApply )
	
	def __del__( self ):
		# Disconnect Events
		self.m_directoryCtl.Unbind( wx.EVT_TREE_SEL_CHANGED, None )
		self.m_reFromCtl.Unbind( wx.EVT_KILL_FOCUS, None )
		self.m_reFromCtl.Unbind( wx.EVT_SET_FOCUS, None )
		self.m_reFromCtl.Unbind( wx.EVT_TEXT, None )
		self.m_reFromCtl.Unbind( wx.EVT_TEXT_ENTER, None )
		self.m_reToCtl.Unbind( wx.EVT_KILL_FOCUS, None )
		self.m_reToCtl.Unbind( wx.EVT_SET_FOCUS, None )
		self.m_reToCtl.Unbind( wx.EVT_TEXT, None )
		self.m_reToCtl.Unbind( wx.EVT_TEXT_ENTER, None )
		self.m_applyBtn.Unbind( wx.EVT_LEFT_DOWN, None )
	
	
	# Virtual event handlers, overide them in your derived class
	def onDirectorySelectionChanged( self, event ):
		event.Skip()
	
	def onUnfocusRegex( self, event ):
		event.Skip()
	
	def onFocusRegex( self, event ):
		event.Skip()
	
	def onTextChange( self, event ):
		event.Skip()
	
	def onHitEnterInFrom( self, event ):
		event.Skip()
	
	
	
	
	def onHitEnterInTo( self, event ):
		event.Skip()
	
	def onApply( self, event ):
		event.Skip()
	

