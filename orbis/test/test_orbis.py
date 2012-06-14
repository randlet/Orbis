import numpy
import orbis
import orbis.gui
import orbis.settings
import os
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
        self.frame.Show()
        
    #---------------------------------------------------------------------------
    def tearDown(self):
        self.frame.Destroy()
        
    #---------------------------------------------------------------------------
    def test_title(self):
        title = self.frame.GetTitle()        
        self.assertEqual(title,orbis.settings.TITLE)
        
if __name__ == "__main__":
    unittest.main()            