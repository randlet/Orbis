import numpy
import shmo
import orbis
import orbis.gui
import orbis.settings
import os
import sys
import unittest
import wx
TEST_PRECISION = 4
#====================================================================================
class Test(unittest.TestCase):
    #---------------------------------------------------------------------------
    def setUp(self):
        
        #change directory to main Orbis package so that relative image imports work
        os.chdir(os.path.join(os.path.dirname(__file__),".."))
        self.app = wx.App(redirect=False)
        self.frame = orbis.MainFrame(parent=None)
        self.data = numpy.matrix("0 -1 -1; -1 0 -1; -1 -1 0")
        #self.frame.Show()
        
    #---------------------------------------------------------------------------
    def tearDown(self):
        self.frame.Destroy()
        
    #---------------------------------------------------------------------------
    def test_title(self):        
        title = self.frame.GetTitle()        
        self.assertEqual(title,orbis.settings.TITLE)
    #---------------------------------------------------------------------------
    def test_unfrozen(self):
        self.assertFalse(orbis.settings.FROZEN)
        self.assertEqual(orbis.settings.ROOT, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    #---------------------------------------------------------------------------
    def test_frozen(self):
        tmp_frozen = getattr(sys,"frozen","")
        setattr(sys,"frozen",True)
        reload(orbis.settings)
        
        self.assertTrue(orbis.settings.FROZEN)
        self.assertEqual(orbis.settings.ROOT,os.path.dirname(sys.executable))
        setattr(sys,"frozen",tmp_frozen)
        reload(orbis.settings)
    #---------------------------------------------------------------------------
    def test_on_num_electrons(self):

        self.frame.solver.set_data(self.data)
        self.frame.num_electrons.SetValue(self.frame.solver.num_electrons+1)
        self.frame.on_huckel_change(None)

        self.assertEqual(self.frame.solver.num_electrons,self.data.shape[0]+1)
    #---------------------------------------------------------------------------
    def test_set_matrix_shape(self):
        shapes = ( (0,0), (1,1), (3,3),)
        for rows,cols in shapes:
            self.frame.set_matrix_shape((rows,cols))
            matrix_rows = self.frame.huckel_grid.NumberRows
            matrix_cols = self.frame.huckel_grid.NumberCols
            self.assertEqual(rows,matrix_rows)
            self.assertEqual(cols,matrix_cols)
    #---------------------------------------------------------------------------
    def test_data_shape_on_set_data(self):
        self.frame.set_huckel_data(self.data)
        g = self.frame.huckel_grid
        self.assertEqual(self.data.shape,(g.GetNumberRows(),g.GetNumberCols()))
    #---------------------------------------------------------------------------
    def test_data_set_correctly(self):
        self.frame.set_huckel_data(self.data)
        print self.data,self.frame.get_huckel_data()
        self.assertTrue((self.data==self.frame.get_huckel_data()).all())
        
if __name__ == "__main__":
    unittest.main()            