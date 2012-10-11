import matplotlib
import matplotlib.patches
import numpy
import wx

from plots import Plot

#====================================================================================
class SketchPad(Plot):
    """sketch pad for drawing molecules"""

    ATOM_RADIUS = 0.1
    PICK_TOLERANCE = 5
    
    #----------------------------------------------------------------------
    def __init__(self,*args,**kwargs):
        super(SketchPad,self).__init__(*args,**kwargs)
        self.axes = self.figure.add_subplot(1,1,1)
        self.axes.set_aspect("equal")
        
    #---------------------------------------------------------------------------
    def on_button_up(self,event):        
        super(SketchPad,self).on_button_up(event)
        
        if self.new_atom_requested():
            self.add_atom()
        

    #---------------------------------------------------------------------------
    def new_atom_requested(self):
        return self.was_click() and not self.was_pick()              
    #---------------------------------------------------------------------------
    def add_atom(self):
        """Add a new atom to the sketchpad"""
        coords = (self.mouse_up_x,self.mouse_up_y)        
        circ = matplotlib.patches.Ellipse(coords,self.ATOM_RADIUS,self.ATOM_RADIUS,picker=self.PICK_TOLERANCE)
        self.axes.add_patch(circ)
        self.figure.canvas.draw()
        
        
if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None)
    sp = SketchPad(frame)
    frame.Show()
    app.MainLoop()
    