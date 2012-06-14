import numpy
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
        self.frame.Show()
        
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
        
if __name__ == "__main__":
    unittest.main()            