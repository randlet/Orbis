import os
import sys

VERSION = (0,1,0)
VERSION_STRING = "v%d.%d.%d" % VERSION
TITLE = "Orbis :: %s" % VERSION_STRING

#setup root directory path
FROZEN = getattr(sys, 'frozen', '')
if not FROZEN: # not frozen: in regular python interpreter
    ROOT = os.path.abspath(os.path.dirname(__file__))
    FROZEN = False
elif FROZEN in ('dll', 'console_exe', 'windows_exe',1): # py2exe/pyinstaller:
    FROZEN = True
    ROOT = os.path.dirname(sys.executable)


sketch = {
    "bond_pick_tolerance":5,
    "bond_line_width":2,
    "atom_radius":0.02,
    "atom_pick_tolerance":5,
    "drag_color":"g",
    "drag_line_style":"--",    
}