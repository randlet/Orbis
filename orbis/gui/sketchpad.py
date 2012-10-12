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
        self.up_atom = None
        self.down_atom = None
    #---------------------------------------------------------------------------
    def on_button_down(self,event):
        super(SketchPad,self).on_button_down(event)
        self.down_atom = self.atom_at_event_point(event)
    #---------------------------------------------------------------------------
    def atom_at_event_point(self,event):
        for patch in self.axes.patches:
            event_in_atom,_ = patch.contains(event)
            if event_in_atom:
                return patch                
    #---------------------------------------------------------------------------
    def on_button_up(self,event):        
        super(SketchPad,self).on_button_up(event)
        
        self.up_atom = self.atom_at_event_point(event)
        
        if self.new_atom_requested():
            self.add_atom()
        elif self.new_bond_requested() and not self.bond_exists(self.up_atom,self.down_atom):
            self.add_bond()
            
    #---------------------------------------------------------------------------
    def on_pick(self,event):
        super(SketchPad,self).on_pick(event)
    #---------------------------------------------------------------------------
    def new_atom_requested(self):
        return self.was_click() and not self.was_pick()              
    #---------------------------------------------------------------------------
    def new_bond_requested(self):        
        start_and_finish_atoms = None not in (self.up_atom, self.down_atom)
        unique_atoms = self.up_atom is not self.down_atom
        return start_and_finish_atoms and unique_atoms
    #---------------------------------------------------------------------------
    def bond_exists(self,atom_1,atom_2):        
        bond_coords = [sorted(bond.get_xydata().tolist()) for bond in self.axes.lines]
        bond_to_check = sorted([list(atom_1.xy),list(atom_2.xy)])
        return bond_to_check in bond_coords
    #---------------------------------------------------------------------------
    def get_atom_locations(self):
        """returns xy points of all atoms on sketchpad"""
        return [atom.xy for atom in self.axes.patches]
    #---------------------------------------------------------------------------
    def add_atom(self):
        """Add a new atom to the sketchpad"""
        coords = (self.mouse_up_x,self.mouse_up_y)        
        circ = matplotlib.patches.CirclePolygon(coords,self.ATOM_RADIUS,picker=self.PICK_TOLERANCE,resolution=40)
        self.axes.add_patch(circ)
        self.figure.canvas.draw()
    #---------------------------------------------------------------------------
    def add_bond(self):
        """add a new bond between down_atom and up_atom"""
        x1,y1 = self.down_atom.xy
        x2,y2 = self.up_atom.xy
        self.axes.plot([x1,x2],[y1,y2])
        self.figure.canvas.draw()
        
if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None)
    sp = SketchPad(frame)
    frame.Show()
    app.MainLoop()
    