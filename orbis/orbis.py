import gui
import gui.grid_utils
import numpy
import settings
import shmo
import sys
import os
os.chdir(os.path.dirname(__file__))
import wx

#====================================================================================
class MainFrame(gui.VOrbisFrame):
    """The main Orbis application frame"""

    #----------------------------------------------------------------------
    def __init__(self,parent,*args, **kwargs):
        """do any initial setup required for Orbis"""
        super(MainFrame,self).__init__(parent,*args,**kwargs)
        self.SetTitle(settings.TITLE)
        self.Layout()
        self.Fit()
        self.Maximize()
                
        self.solver = shmo.HuckelSolver()
    #---------------------------------------------------------------------------
    def on_huckel_change(self,event):
        """some parameter of molecule has been changed, update solver"""
        num_electrons = self.num_electrons.GetValue()
        data = self.get_huckel_data()

        self.solver.set_data(data,num_electrons=num_electrons)
    #---------------------------------------------------------------------------
    def get_huckel_data(self):
        """return current atom/bond matrix for solver"""
        shape = gui.grid_utils.get_shape(self.huckel_grid)
        data = numpy.zeros(shape)
        for row in range(shape[0]):
            for col in range(shape[1]):
                try:
                    data[row, col] = float(self.huckel_grid.GetCellValue(row,col).strip())
                except (TypeError,ValueError):
                    data[row, col] = 0.
                  
        return numpy.matrix(data)
    #---------------------------------------------------------------------------
    def set_huckel_data(self,data):
        """set huckel matrix to input data"""
        self.set_matrix_shape(data.shape)
        rows,cols = data.shape
        for row in range(rows):
            for col in range(cols): 
                self.huckel_grid.SetCellValue(row,col,"{0}".format(data[row,col]))
    #---------------------------------------------------------------------------
    def set_matrix_shape(self,shape):
        """set the huckel matrix shape"""
        gui.grid_utils.set_shape(self.huckel_grid,shape)
        
#----------------------------------------------------------------------
def main():
    """Launch the main program"""
    app = wx.App(useBestVisual=True)
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()    
    
if __name__ == "__main__":
    main()