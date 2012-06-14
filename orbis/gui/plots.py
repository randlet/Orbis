import wx

import matplotlib
matplotlib.use("WXAgg")
import matplotlib.figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as Canvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2Wx as Toolbar
from matplotlib.widgets import SpanSelector

class Plot(wx.Panel):
    def __init__(self, parent, id = -1, dpi = None, **kwargs):
        wx.Panel.__init__(self, parent, id=id, **kwargs)
        self.figure = matplotlib.figure.Figure(dpi=dpi, figsize=(2,2))

        self.canvas = Canvas(self, -1, self.figure)
        self.toolbar = Toolbar(self.canvas)
        self.toolbar.Realize()

        self.plot_sizer = wx.BoxSizer(wx.VERTICAL)
        self.plot_sizer.Add(self.toolbar, 0,wx.ALIGN_CENTER_VERTICAL|wx.EXPAND)
        self.plot_sizer.Add(self.canvas,1,wx.EXPAND)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.plot_sizer,1,wx.EXPAND)
        self.SetSizer(self.sizer)


#====================================================================================
class SketchPad(Plot):
    """sketch pad for drawing molecules"""

    #----------------------------------------------------------------------
    def __init__(self,*args,**kwargs):
        super(SketchPad,self).__init__(*args,**kwargs)
        
#====================================================================================
class EnergyLevelDiagram(Plot):
    """sketch pad for drawing molecules"""

    #----------------------------------------------------------------------
    def __init__(self,*args,**kwargs):
        super(EnergyLevelDiagram,self).__init__(*args,**kwargs)
    
#====================================================================================
class OrbitalDiagram(Plot):
    """figure for showing the orbital diagram"""

    #----------------------------------------------------------------------
    def __init__(self,*args,**kwargs):
        super(OrbitalDiagram,self).__init__(*args,**kwargs)
        
        
    
    
