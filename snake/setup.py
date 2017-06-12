import os
#os.environ['TCL_LIBRARY']="C:\\Users\\User\\AppData\\Local\\Programs\\Python36]]tcl]]tcl8.6"
#os.environ['TK_LIBRARY']="C:\\Users\\User\\AppData\\Local\\Programs\\Python36]]tcl]]tcl8.6"
os.environ['TCL_LIBRARY']="C:\\Tcl\\include\\tcl8.6"
os.environ['TK_LIBRARY']="C:\\Tcl\\include\\tk8.6"


import cx_Freeze 

executables = [
        
        cx_Freeze.Executable("1.py") 
] 
cx_Freeze.setup( 
        name = "Pygame Snake", 
        options = {"build_exe": {"packages":["pygame"],"include_files":["logo.png","snake.png","apple.png"]}},
        description = "Snake made with pygame", 
executables = executables)