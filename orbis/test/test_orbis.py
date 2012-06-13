import orbis
import orbis.gui
import os
import numpy
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
    #---------------------------------------------------------------------------
    def tearDown(self):
        self.frame.Destroy()
        
    #---------------------------------------------------------------------------
    def test1(self):
        """"""
        self.assertEqual(1,1)
if __name__ == "__main__":
    unittest.main()            