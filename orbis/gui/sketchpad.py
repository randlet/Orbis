import matplotlib
import matplotlib.patches
import settings
import numpy
import wx

from plots import Plot

#====================================================================================
class SketchPad(Plot):
    """sketch pad for drawing molecules"""

    PICK_TOLERANCE = 5
    
    #----------------------------------------------------------------------
    def __init__(self,*args,**kwargs):
        super(SketchPad,self).__init__(*args,**kwargs)

        self.setup_axes()
        
        self.drag_line = None
        self.up_atom = None
        self.down_atom = None
        
    #---------------------------------------------------------------------------
    def setup_axes(self):
        """initial config for self.axes"""
        self.axes = self.figure.add_subplot(1,1,1)
        self.axes.set_aspect("equal")
        self.axes.set_autoscale_on(False)
        
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

        if self.drag_line:
            self.delete_drag_line()
        
        self.up_atom = self.atom_at_event_point(event)
        
        if self.new_atom_requested():
            self.add_atom()
        elif self.new_bond_requested() and not self.bond_exists(self.up_atom,self.down_atom):
            self.add_bond()
            
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

        circ = matplotlib.patches.CirclePolygon(
            coords,
            settings.sketch["atom_radius"],
            picker=settings.sketch["pick_tolerance"],
            resolution=40,
            color = self.get_atom_color(),
        )
        self.axes.add_patch(circ)
        self.figure.canvas.draw()
    #---------------------------------------------------------------------------
    def add_bond(self):
        """add a new bond between down_atom and up_atom"""
        x1,y1 = self.down_atom.xy
        x2,y2 = self.up_atom.xy
        self.axes.plot([x1,x2],[y1,y2],color=self.get_bond_color(),linewidth=settings.sketch["bond_line_width"])
        self.figure.canvas.draw()
    #---------------------------------------------------------------------------
    def get_atom_color(self):
        """return color of atom to draw"""
        return "r"
    #---------------------------------------------------------------------------
    def get_bond_color(self):
        """return color of bond to draw"""
        return "b"
    #---------------------------------------------------------------------------
    def on_pick(self,event):
        super(SketchPad,self).on_pick(event)
    #---------------------------------------------------------------------------
    def on_motion(self,event):
        """draw line if user creating bond"""
        super(SketchPad,self).on_motion(event)

        multiple_atoms = len(self.axes.patches) > 1
        
        if event.button is not None and self.down_atom is not None and multiple_atoms:
            xs = [self.down_atom.xy[0],event.xdata]
            ys = [self.down_atom.xy[1],event.ydata]

            if self.drag_line is None:                
                self.drag_line = self.axes.plot(xs,ys,color=settings.sketch["drag_color"],linestyle=settings.sketch["drag_line_style"])[0]
            else:
                self.drag_line.set_data(xs,ys)
                
            self.figure.canvas.draw()
    #---------------------------------------------------------------------------
    def delete_drag_line(self):
        self.axes.lines.remove(self.drag_line)
        del self.drag_line
        self.drag_line = None
        
if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None)
    sp = SketchPad(frame)
    frame.Show()
    app.MainLoop()
    