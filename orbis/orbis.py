import gui
import settings
import sys
import os
os.chdir(os.path.dirname(__file__))


#====================================================================================
class MainFrame(gui.VOrbisFrame):
    """The main Orbis application frame"""

    #----------------------------------------------------------------------
    def __init__(self,*args, **kwargs):
        """do any initial setup required for Orbis"""
        super(MainFrame,self).__init__(*args,**kwargs)
        
        self.SetTitle(settings.TITLE)
        
        

    