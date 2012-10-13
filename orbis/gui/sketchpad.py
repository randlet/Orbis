import matplotlib
import matplotlib.patches
import settings
import numpy
import wx

from plots import Plot

#====================================================================================
class SketchPad(Plot):
    """sketch pad for drawing molecules"""

    #----------------------------------------------------------------------
    def __init__(self,*args,**kwargs):
        self.refresh_required = False
        
        super(SketchPad,self).__init__(*args,**kwargs)

        self.setup_axes()
        
        self.drag_line = None
        self.up_atom = None
        self.down_atom = None
        self.selected_bond = None
        self.rotation = 0.
    #---------------------------------------------------------------------------
    def setup_axes(self):
        """initial config for self.axes"""
        self.axes = self.figure.add_subplot(1,1,1)
        self.axes.set_aspect("equal")
        self.axes.set_xlim(-1,1)
        self.axes.set_ylim(-1,1)        
        self.axes.set_autoscale_on(False)
    #---------------------------------------------------------------------------
    def on_idle(self,event):
        if self.refresh_required:
            self.figure.canvas.draw()
            self.refresh_required = False
        
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
        elif self.delete_atom_requested(event):
            self.delete_atom(self.up_atom)
        elif self.new_bond_requested():
            self.add_bond()
        elif self.delete_bond_requested(event):
            self.delete_bond(self.selected_bond)
            
    #---------------------------------------------------------------------------
    def new_atom_requested(self):
        return self.was_click() and not self.was_pick()              
    #---------------------------------------------------------------------------
    def delete_atom_requested(self,event):
        return event.key == "control" and self.was_pick() and self.up_atom    
    #---------------------------------------------------------------------------
    def new_bond_requested(self):        
        """check if user requested a new bond"""
        if None in (self.up_atom, self.down_atom):
            return False
        
        unique_atoms = self.up_atom is not self.down_atom
        is_new = not self.bond_exists(self.up_atom,self.down_atom)
        return unique_atoms and is_new
    #---------------------------------------------------------------------------
    def delete_bond_requested(self,event):
        """check if user wants to delete a bond"""
        return event.key == "control" and self.selected_bond 
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
            picker=settings.sketch["atom_pick_tolerance"],
            resolution=40,
            color = self.get_atom_color(),
        )
        self.axes.add_patch(circ)
        self.refresh_required = True
    #---------------------------------------------------------------------------
    def add_bond(self):
        """add a new bond between down_atom and up_atom"""
        x1,y1 = self.down_atom.xy
        x2,y2 = self.up_atom.xy
        self.axes.plot(
            [x1,x2],
            [y1,y2],
            color=self.get_bond_color(),
            linewidth=settings.sketch["bond_line_width"],
            picker=settings.sketch["bond_pick_tolerance"],
        )
        self.refresh_required = True
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

        self.selected_bond = None

        bond_picked = event.artist in self.axes.lines
        if bond_picked:
            self.selected_bond = event.artist
            
    #---------------------------------------------------------------------------
    def on_motion(self,event):
        """draw line if user creating bond"""
        super(SketchPad,self).on_motion(event)

        multiple_atoms = len(self.axes.patches) > 1

        if event.button == 1 and self.down_atom is not None and multiple_atoms:

            xs = [self.down_atom.xy[0],event.xdata]
            ys = [self.down_atom.xy[1],event.ydata]

            if self.drag_line is None:                
                self.drag_line = self.axes.plot(
                    xs,ys,
                    color=settings.sketch["drag_color"],
                    linestyle=settings.sketch["drag_line_style"],                    
                )[0]
            else:
                self.drag_line.set_data(xs,ys)
                
            self.figure.canvas.draw()
    #---------------------------------------------------------------------------
    def on_scroll(self,event):
        """rotate/zoom on scroll"""

        if event.key == "control":
            self.zoom(event.step)
        else:
            self.rotate(event.step)
    #---------------------------------------------------------------------------
    def zoom(self, factor):
        """zoom in (factor > 0) or out (factor < 0)"""
    #---------------------------------------------------------------------------
    def rotate(self,factor):
        """rotate counter clockwise (factor > 0) or clockwise (factor < 0)"""
            
        dt = numpy.deg2rad(factor)
        rot = numpy.mat([[numpy.cos(dt),-numpy.sin(dt)],[numpy.sin(dt),numpy.cos(dt)]])
        xo,yo = self.get_centroid()
        
        def rotate_point(x,y):
            new_pos = rot*(numpy.array((x-xo,y-yo)).reshape((2,1)))
            return xo+new_pos[0,0],yo+new_pos[1,0]
        
        for atom in self.axes.patches:
            atom.xy = rotate_point(*atom.xy)
            
        for bond in self.axes.lines:
            start,finish = [rotate_point(*p) for p in bond.get_xydata()]
            xs, ys = zip(*[start,finish])
            bond.set_xdata(xs)
            bond.set_ydata(ys)
                                     
        self.refresh_required = True
    #---------------------------------------------------------------------------
    def get_centroid(self):
        """return average position of all atoms on sketchpad"""
        xs,ys = zip(*[atom.xy for atom in self.axes.patches])
        return numpy.average(xs),numpy.average(ys)
    #---------------------------------------------------------------------------
    def delete_drag_line(self):
        """clear the temp line from drawing bonds"""
        self.axes.lines.remove(self.drag_line)
        del self.drag_line
        self.drag_line = None
        self.refresh_required = True
    #---------------------------------------------------------------------------
    def delete_atom(self,atom):
        """remove atom and all associated bonds from sketchpad"""
        self.clear_bonds_for_atom(atom)
        self.axes.patches.remove(atom)
        del atom
        self.refresh_required = True
    #---------------------------------------------------------------------------
    def clear_bonds_for_atom(self,atom):
        """delete all lines attached to input atom"""
        position = atom.xy
        to_delete = [bond for bond in self.axes.lines if position in bond.get_xydata()]
        
        for bond in to_delete:
            self.delete_bond(bond)
            
        self.refresh_required = True
    #---------------------------------------------------------------------------
    def delete_bond(self,bond):
        """remove bond from sketchpad"""
        self.axes.lines.remove(bond)
        del bond
        self.selected_bond = None        
        self.refresh_required = True
        
if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None)
    sp = SketchPad(frame)
    frame.Show()
    app.MainLoop()
    