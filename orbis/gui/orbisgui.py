# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import plots
import wx.grid

###########################################################################
## Class VOrbisFrame
###########################################################################

class VOrbisFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Orbis", pos = wx.DefaultPosition, size = wx.Size( 1164,689 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.main_menu_bar = wx.MenuBar( 0 )
		self.file_menu = wx.Menu()
		self.new = wx.MenuItem( self.file_menu, wx.ID_ANY, u"&New"+ u"\t" + u"Ctrl+N", u"New simulation", wx.ITEM_NORMAL )
		self.file_menu.AppendItem( self.new )
		
		self.open = wx.MenuItem( self.file_menu, wx.ID_ANY, u"&Open..."+ u"\t" + u"Ctrl+O", u"Open a previously save simulation", wx.ITEM_NORMAL )
		self.file_menu.AppendItem( self.open )
		
		self.save = wx.MenuItem( self.file_menu, wx.ID_ANY, u"&Save"+ u"\t" + u"Ctrl+S", u"Save the current simulation", wx.ITEM_NORMAL )
		self.file_menu.AppendItem( self.save )
		
		self.save_as = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Save &As..."+ u"\t" + u"Ctrl+Shift+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu.AppendItem( self.save_as )
		
		self.file_menu.AppendSeparator()
		
		self.import_geometry = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Import &Geometry Data..."+ u"\t" + u"Ctrl+G", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu.AppendItem( self.import_geometry )
		
		self.import_huckel = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Import Hückel Matrix Data..."+ u"\t" + u"Ctrl+I", u"Import a Hückel matrix from a csv file", wx.ITEM_NORMAL )
		self.file_menu.AppendItem( self.import_huckel )
		
		self.export = wx.MenuItem( self.file_menu, wx.ID_ANY, u"&Export Results"+ u"\t" + u"Ctrl+E", u"Export simulation results as a csv file ", wx.ITEM_NORMAL )
		self.file_menu.AppendItem( self.export )
		
		self.file_menu.AppendSeparator()
		
		self.quit = wx.MenuItem( self.file_menu, wx.ID_ANY, u"&Quit"+ u"\t" + u"Ctrl+Q", u"Quit Orbis", wx.ITEM_NORMAL )
		self.file_menu.AppendItem( self.quit )
		
		self.main_menu_bar.Append( self.file_menu, u"&File" ) 
		
		self.edit_menu = wx.Menu()
		self.main_menu_bar.Append( self.edit_menu, u"&Edit" ) 
		
		self.tools_menu = wx.Menu()
		self.atoms_menu = wx.MenuItem( self.tools_menu, wx.ID_ANY, u"Edit &Atoms..."+ u"\t" + u"Ctrl+Shift+A", u"Manage available atom types", wx.ITEM_NORMAL )
		self.tools_menu.AppendItem( self.atoms_menu )
		
		self.bonds_menu = wx.MenuItem( self.tools_menu, wx.ID_ANY, u"Edit &Bonds..."+ u"\t" + u"Ctrl+Shift+B", u"Manage available bond types", wx.ITEM_NORMAL )
		self.tools_menu.AppendItem( self.bonds_menu )
		
		self.main_menu_bar.Append( self.tools_menu, u"&Tools" ) 
		
		self.help_menu = wx.Menu()
		self.about = wx.MenuItem( self.help_menu, wx.ID_ANY, u"&About...", u"Information about Orbis", wx.ITEM_NORMAL )
		self.help_menu.AppendItem( self.about )
		
		self.documentation = wx.MenuItem( self.help_menu, wx.ID_ANY, u"&Documentation..."+ u"\t" + u"Ctrl+Shift+D", u"Read the Orbis documentation", wx.ITEM_NORMAL )
		self.help_menu.AppendItem( self.documentation )
		
		self.main_menu_bar.Append( self.help_menu, u"&Help" ) 
		
		self.SetMenuBar( self.main_menu_bar )
		
		self.toolbar = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"images/new16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Clear the current simulation", u"Clear the current simulation", None ) 
		
		self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"images/open16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"images/save16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Save the current simularion", u"Save the current simularion", None ) 
		
		self.toolbar.Realize() 
		
		main_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.controls = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		controls_sizer = wx.BoxSizer( wx.VERTICAL )
		
		huckel_control_sizer = wx.StaticBoxSizer( wx.StaticBox( self.controls, wx.ID_ANY, u"Hückel Controls" ), wx.VERTICAL )
		
		basis_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		basis_sizer.AddGrowableCol( 1 )
		basis_sizer.SetFlexibleDirection( wx.HORIZONTAL )
		basis_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.num_electrons_label = wx.StaticText( self.controls, wx.ID_ANY, u"Num Electrons:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.num_electrons_label.Wrap( -1 )
		basis_sizer.Add( self.num_electrons_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.num_electrons = wx.SpinCtrl( self.controls, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 48,-1 ), wx.SP_ARROW_KEYS, 0, 100, 0 )
		self.num_electrons.SetToolTipString( u"Set the number of electrons" )
		
		basis_sizer.Add( self.num_electrons, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.basis_size_label = wx.StaticText( self.controls, wx.ID_ANY, u"Basis Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.basis_size_label.Wrap( -1 )
		basis_sizer.Add( self.basis_size_label, 0, wx.ALL, 5 )
		
		self.basis_size = wx.SpinCtrl( self.controls, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 48,-1 ), wx.SP_ARROW_KEYS, 0, 100, 0 )
		self.basis_size.SetToolTipString( u"Set the basis size of the Huckel matrix" )
		
		basis_sizer.Add( self.basis_size, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		huckel_control_sizer.Add( basis_sizer, 1, wx.EXPAND, 5 )
		
		atom_typeChoices = []
		self.atom_type = wx.Choice( self.controls, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, atom_typeChoices, 0 )
		self.atom_type.SetSelection( 0 )
		self.atom_type.SetToolTipString( u"Choose an atom type" )
		
		huckel_control_sizer.Add( self.atom_type, 0, wx.ALL|wx.EXPAND, 5 )
		
		controls_sizer.Add( huckel_control_sizer, 0, wx.EXPAND|wx.ALL, 5 )
		
		sketch_pad_control_sizer = wx.StaticBoxSizer( wx.StaticBox( self.controls, wx.ID_ANY, u"Sketch Pad Controls" ), wx.VERTICAL )
		
		sketch_pad_control_sub_sizer = wx.GridSizer( 0, 3, 0, 0 )
		
		self.zoom_label = wx.StaticText( self.controls, wx.ID_ANY, u"Zoom:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.zoom_label.Wrap( -1 )
		sketch_pad_control_sub_sizer.Add( self.zoom_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.zoom_in = wx.Button( self.controls, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		sketch_pad_control_sub_sizer.Add( self.zoom_in, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.zoom_out = wx.Button( self.controls, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		sketch_pad_control_sub_sizer.Add( self.zoom_out, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.rotate_label = wx.StaticText( self.controls, wx.ID_ANY, u"Rotate:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rotate_label.Wrap( -1 )
		sketch_pad_control_sub_sizer.Add( self.rotate_label, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.rotate_cw = wx.Button( self.controls, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		sketch_pad_control_sub_sizer.Add( self.rotate_cw, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.rotate_ccw = wx.Button( self.controls, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		sketch_pad_control_sub_sizer.Add( self.rotate_ccw, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sketch_pad_control_sub_sizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.redraw = wx.Button( self.controls, wx.ID_ANY, u"Redraw", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.redraw.SetToolTipString( u"Normalize the molecules shape" )
		
		sketch_pad_control_sub_sizer.Add( self.redraw, 0, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.clear = wx.Button( self.controls, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		sketch_pad_control_sub_sizer.Add( self.clear, 0, wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sketch_pad_control_sizer.Add( sketch_pad_control_sub_sizer, 1, wx.EXPAND, 5 )
		
		controls_sizer.Add( sketch_pad_control_sizer, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.controls.SetSizer( controls_sizer )
		self.controls.Layout()
		controls_sizer.Fit( self.controls )
		main_sizer.Add( self.controls, 0, wx.EXPAND, 5 )
		
		self.main_splitter = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.plots_container = wx.Panel( self.main_splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		plot_container_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.sketch_pad =  plots.SketchPad(self.plots_container)
		plot_container_sizer.Add( self.sketch_pad, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.results_plot_splitter = wx.SplitterWindow( self.plots_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.results_plot_splitter.Bind( wx.EVT_IDLE, self.results_plot_splitterOnIdle )
		
		self.eld_plot_container = wx.Panel( self.results_plot_splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		eld_plot_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.eld_plot = plots.EnergyLevelDiagram(self.eld_plot_container)
		eld_plot_sizer.Add( self.eld_plot, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.eld_plot_container.SetSizer( eld_plot_sizer )
		self.eld_plot_container.Layout()
		eld_plot_sizer.Fit( self.eld_plot_container )
		self.orbital_plot_container = wx.Panel( self.results_plot_splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		orbital_plot_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.orbital_plot = plots.OrbitalDiagram(self.orbital_plot_container)
		orbital_plot_sizer.Add( self.orbital_plot, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.orbital_plot_container.SetSizer( orbital_plot_sizer )
		self.orbital_plot_container.Layout()
		orbital_plot_sizer.Fit( self.orbital_plot_container )
		self.results_plot_splitter.SplitVertically( self.eld_plot_container, self.orbital_plot_container, 0 )
		plot_container_sizer.Add( self.results_plot_splitter, 1, wx.EXPAND, 5 )
		
		self.plots_container.SetSizer( plot_container_sizer )
		self.plots_container.Layout()
		plot_container_sizer.Fit( self.plots_container )
		self.grids_container = wx.Panel( self.main_splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		grids_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.huckel_notebook = wx.Notebook( self.grids_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.huckel_container = wx.Panel( self.huckel_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		huckel_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.huckel_grid = wx.grid.Grid( self.huckel_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.huckel_grid.CreateGrid( 5, 5 )
		self.huckel_grid.EnableEditing( True )
		self.huckel_grid.EnableGridLines( True )
		self.huckel_grid.EnableDragGridSize( False )
		self.huckel_grid.SetMargins( 0, 0 )
		
		# Columns
		self.huckel_grid.EnableDragColMove( False )
		self.huckel_grid.EnableDragColSize( True )
		self.huckel_grid.SetColLabelSize( 30 )
		self.huckel_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.huckel_grid.EnableDragRowSize( True )
		self.huckel_grid.SetRowLabelSize( 80 )
		self.huckel_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.huckel_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		huckel_sizer.Add( self.huckel_grid, 1, wx.EXPAND, 5 )
		
		self.huckel_container.SetSizer( huckel_sizer )
		self.huckel_container.Layout()
		huckel_sizer.Fit( self.huckel_container )
		self.huckel_notebook.AddPage( self.huckel_container, u"Hückel Matrix", False )
		
		grids_sizer.Add( self.huckel_notebook, 1, wx.EXPAND, 5 )
		
		self.results_notebook = wx.Notebook( self.grids_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.eigen_container = wx.Panel( self.results_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		eigen_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.eigen_grid = wx.grid.Grid( self.eigen_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.eigen_grid.CreateGrid( 5, 5 )
		self.eigen_grid.EnableEditing( False )
		self.eigen_grid.EnableGridLines( True )
		self.eigen_grid.EnableDragGridSize( False )
		self.eigen_grid.SetMargins( 0, 0 )
		
		# Columns
		self.eigen_grid.EnableDragColMove( False )
		self.eigen_grid.EnableDragColSize( True )
		self.eigen_grid.SetColLabelSize( 30 )
		self.eigen_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.eigen_grid.EnableDragRowSize( True )
		self.eigen_grid.SetRowLabelSize( 80 )
		self.eigen_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.eigen_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		eigen_sizer.Add( self.eigen_grid, 1, wx.EXPAND, 5 )
		
		self.eigen_container.SetSizer( eigen_sizer )
		self.eigen_container.Layout()
		eigen_sizer.Fit( self.eigen_container )
		self.results_notebook.AddPage( self.eigen_container, u"Eigenvectors", True )
		self.bond_order_containers = wx.Panel( self.results_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bond_order_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.bond_order_grid = wx.grid.Grid( self.bond_order_containers, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.bond_order_grid.CreateGrid( 5, 5 )
		self.bond_order_grid.EnableEditing( False )
		self.bond_order_grid.EnableGridLines( True )
		self.bond_order_grid.EnableDragGridSize( False )
		self.bond_order_grid.SetMargins( 0, 0 )
		
		# Columns
		self.bond_order_grid.EnableDragColMove( False )
		self.bond_order_grid.EnableDragColSize( True )
		self.bond_order_grid.SetColLabelSize( 30 )
		self.bond_order_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.bond_order_grid.EnableDragRowSize( True )
		self.bond_order_grid.SetRowLabelSize( 80 )
		self.bond_order_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.bond_order_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bond_order_sizer.Add( self.bond_order_grid, 1, wx.EXPAND, 5 )
		
		self.bond_order_containers.SetSizer( bond_order_sizer )
		self.bond_order_containers.Layout()
		bond_order_sizer.Fit( self.bond_order_containers )
		self.results_notebook.AddPage( self.bond_order_containers, u"Π Bond Orders", False )
		self.charge_container = wx.Panel( self.results_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		charge_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.charge_grid = wx.grid.Grid( self.charge_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.charge_grid.CreateGrid( 5, 5 )
		self.charge_grid.EnableEditing( False )
		self.charge_grid.EnableGridLines( True )
		self.charge_grid.EnableDragGridSize( False )
		self.charge_grid.SetMargins( 0, 0 )
		
		# Columns
		self.charge_grid.EnableDragColMove( False )
		self.charge_grid.EnableDragColSize( True )
		self.charge_grid.SetColLabelSize( 30 )
		self.charge_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.charge_grid.EnableDragRowSize( True )
		self.charge_grid.SetRowLabelSize( 80 )
		self.charge_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.charge_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		charge_sizer.Add( self.charge_grid, 0, wx.ALL, 5 )
		
		self.charge_container.SetSizer( charge_sizer )
		self.charge_container.Layout()
		charge_sizer.Fit( self.charge_container )
		self.results_notebook.AddPage( self.charge_container, u"Charge Densities", False )
		self.aa_polar_container = wx.Panel( self.results_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		aa_polar_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.aa_polar_grid = wx.grid.Grid( self.aa_polar_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.aa_polar_grid.CreateGrid( 5, 5 )
		self.aa_polar_grid.EnableEditing( False )
		self.aa_polar_grid.EnableGridLines( True )
		self.aa_polar_grid.EnableDragGridSize( False )
		self.aa_polar_grid.SetMargins( 0, 0 )
		
		# Columns
		self.aa_polar_grid.EnableDragColMove( False )
		self.aa_polar_grid.EnableDragColSize( True )
		self.aa_polar_grid.SetColLabelSize( 30 )
		self.aa_polar_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.aa_polar_grid.EnableDragRowSize( True )
		self.aa_polar_grid.SetRowLabelSize( 80 )
		self.aa_polar_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.aa_polar_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		aa_polar_sizer.Add( self.aa_polar_grid, 0, wx.ALL, 5 )
		
		self.aa_polar_container.SetSizer( aa_polar_sizer )
		self.aa_polar_container.Layout()
		aa_polar_sizer.Fit( self.aa_polar_container )
		self.results_notebook.AddPage( self.aa_polar_container, u"A-A Polarizabilities", False )
		self.ab_polar_container = wx.Panel( self.results_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		ab_polar_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.ab_polar_grid = wx.grid.Grid( self.ab_polar_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.ab_polar_grid.CreateGrid( 5, 5 )
		self.ab_polar_grid.EnableEditing( False )
		self.ab_polar_grid.EnableGridLines( True )
		self.ab_polar_grid.EnableDragGridSize( False )
		self.ab_polar_grid.SetMargins( 0, 0 )
		
		# Columns
		self.ab_polar_grid.EnableDragColMove( False )
		self.ab_polar_grid.EnableDragColSize( True )
		self.ab_polar_grid.SetColLabelSize( 30 )
		self.ab_polar_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.ab_polar_grid.EnableDragRowSize( True )
		self.ab_polar_grid.SetRowLabelSize( 80 )
		self.ab_polar_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.ab_polar_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		ab_polar_sizer.Add( self.ab_polar_grid, 0, wx.ALL, 5 )
		
		self.ab_polar_container.SetSizer( ab_polar_sizer )
		self.ab_polar_container.Layout()
		ab_polar_sizer.Fit( self.ab_polar_container )
		self.results_notebook.AddPage( self.ab_polar_container, u"A-B Polarizabilities", False )
		
		grids_sizer.Add( self.results_notebook, 1, wx.EXPAND, 5 )
		
		self.grids_container.SetSizer( grids_sizer )
		self.grids_container.Layout()
		grids_sizer.Fit( self.grids_container )
		self.main_splitter.SplitVertically( self.plots_container, self.grids_container, -1 )
		main_sizer.Add( self.main_splitter, 1, wx.EXPAND, 5 )
		
		self.SetSizer( main_sizer )
		self.Layout()
		self.status_bar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.on_new, id = self.new.GetId() )
		self.Bind( wx.EVT_MENU, self.on_open, id = self.open.GetId() )
		self.Bind( wx.EVT_MENU, self.on_save, id = self.save.GetId() )
		self.Bind( wx.EVT_MENU, self.on_save_as, id = self.save_as.GetId() )
		self.Bind( wx.EVT_MENU, self.on_import_geom, id = self.import_geometry.GetId() )
		self.Bind( wx.EVT_MENU, self.on_quit, id = self.quit.GetId() )
		self.Bind( wx.EVT_MENU, self.on_atoms, id = self.atoms_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.on_bonds, id = self.bonds_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.on_about, id = self.about.GetId() )
		self.Bind( wx.EVT_MENU, self.on_documentation, id = self.documentation.GetId() )
		self.Bind( wx.EVT_TOOL, self.on_new, id = wx.ID_ANY )
		self.Bind( wx.EVT_TOOL_ENTER, self.on_new, id = wx.ID_ANY )
		self.Bind( wx.EVT_TOOL, self.on_open, id = wx.ID_ANY )
		self.Bind( wx.EVT_TOOL_ENTER, self.on_open, id = wx.ID_ANY )
		self.Bind( wx.EVT_TOOL, self.on_save, id = wx.ID_ANY )
		self.Bind( wx.EVT_TOOL_ENTER, self.on_save, id = wx.ID_ANY )
		self.num_electrons.Bind( wx.EVT_SPINCTRL, self.on_huckel_change )
		self.basis_size.Bind( wx.EVT_SPINCTRL, self.on_huckel_change )
		self.basis_size.Bind( wx.EVT_TEXT, self.on_huckel_change )
		self.atom_type.Bind( wx.EVT_CHOICE, self.on_atom_change )
		self.zoom_in.Bind( wx.EVT_BUTTON, self.on_zoom )
		self.zoom_out.Bind( wx.EVT_BUTTON, self.on_zoom )
		self.redraw.Bind( wx.EVT_BUTTON, self.on_redraw )
		self.clear.Bind( wx.EVT_BUTTON, self.on_clear )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_new( self, event ):
		event.Skip()
	
	def on_open( self, event ):
		event.Skip()
	
	def on_save( self, event ):
		event.Skip()
	
	def on_save_as( self, event ):
		event.Skip()
	
	def on_import_geom( self, event ):
		event.Skip()
	
	def on_quit( self, event ):
		event.Skip()
	
	def on_atoms( self, event ):
		event.Skip()
	
	def on_bonds( self, event ):
		event.Skip()
	
	def on_about( self, event ):
		event.Skip()
	
	def on_documentation( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	def on_huckel_change( self, event ):
		event.Skip()
	
	
	
	def on_atom_change( self, event ):
		event.Skip()
	
	def on_zoom( self, event ):
		event.Skip()
	
	
	def on_redraw( self, event ):
		event.Skip()
	
	def on_clear( self, event ):
		event.Skip()
	
	def results_plot_splitterOnIdle( self, event ):
		self.results_plot_splitter.SetSashPosition( 0 )
		self.results_plot_splitter.Unbind( wx.EVT_IDLE )
	

