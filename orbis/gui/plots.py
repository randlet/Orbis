

import matplotlib; matplotlib.use("WXAgg")
import matplotlib.figure
import numpy
import wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as Canvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2Wx as Toolbar
from matplotlib.widgets import SpanSelector

class Plot(wx.Panel):
    def __init__(self, parent, id = -1, dpi = None,toolbar=True, **kwargs):
        wx.Panel.__init__(self, parent, id=id, **kwargs)
        self.figure = matplotlib.figure.Figure(dpi=dpi, facecolor=(0.9,0.9,0.9,1))

        self.canvas = Canvas(self, -1, self.figure)
        self.plot_sizer = wx.BoxSizer(wx.VERTICAL)

        if toolbar:
            self.toolbar = Toolbar(self.canvas)
            self.toolbar.Realize()            
            self.plot_sizer.Add(self.toolbar, 0,wx.ALIGN_CENTER_VERTICAL|wx.EXPAND)
            
        self.plot_sizer.Add(self.canvas,1,wx.EXPAND)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.plot_sizer,1,wx.EXPAND)
        self.SetSizer(self.sizer)
        
        self.setup_events()
        
    #---------------------------------------------------------------------------
    def setup_events(self):

        self.mouse_down_x = None
        self.mouse_down_y = None
        self.mouse_up_x = None
        self.mouse_up_y = None
        self.pick_x = None
        self.pick_y = None
        
        self.set_event_handlers()
    #---------------------------------------------------------------------------
    def set_event_handlers(self):
        """wire up default mpl event handlers"""
        events = (
            ("button_press_event",self.on_button_down),
            ("button_release_event",self.on_button_up),
            ("key_press_event",self.on_key_down),
            ("key_release_event",self.on_key_up),
            ("pick_event",self.on_pick),
            ("motion_notify_event",self.on_motion),
            ("scroll_event",self.on_scroll),
        )
            
        for event, handler in events:            
            self.figure.canvas.mpl_connect(event,handler)
    #---------------------------------------------------------------------------
    def on_button_down(self,event):
        """default button down handler"""        
        self.mouse_down_x = event.xdata
        self.mouse_down_y = event.ydata            
    #---------------------------------------------------------------------------
    def on_button_up(self,event):        
        """default button up handler"""
        self.mouse_up_x = event.xdata
        self.mouse_up_y = event.ydata
    #---------------------------------------------------------------------------
    def on_pick(self,event):
        """default pick event"""
        self.pick_x = event.mouseevent.xdata
        self.pick_y = event.mouseevent.ydata            
    #---------------------------------------------------------------------------
    def on_key_down(self,event):
        """default key down event"""
    #---------------------------------------------------------------------------
    def on_key_up(self,event):
        """default key up event"""
    #---------------------------------------------------------------------------
    def on_motion(self,event):
        """default mouse motion event"""
    #---------------------------------------------------------------------------
    def on_scroll(self,event):
        """default scroll event"""        
        
    #---------------------------------------------------------------------------
    def was_click(self):
        """check whether mouse down/up are coincident and therfore qualify as a click"""
        if None in (self.mouse_down_x, self.mouse_down_y, self.mouse_up_x, self.mouse_up_y):
            return False
        downs = (self.mouse_down_x, self.mouse_down_y)
        ups = (self.mouse_up_x, self.mouse_up_y)
        
        return numpy.allclose(downs,ups)
    #---------------------------------------------------------------------------
    def was_pick(self):
        """check if last click was an artist pick"""
        if None in (self.pick_x,self.pick_y,self.mouse_up_x,self.mouse_up_y):
            return False
        picks = (self.pick_x,self.pick_y)
        ups = (self.mouse_up_x,self.mouse_up_y)
        return numpy.allclose(picks,ups)

        
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
        
        
    
    
