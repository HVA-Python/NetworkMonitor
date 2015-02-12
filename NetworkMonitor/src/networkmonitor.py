#!/usr/bin/env python3
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import curses #GUI interface

myscreen = curses.initscr() #Initialize GUI

myscreen.border(0) #GUI border
myscreen.addstr(12, 25, "Welkom bij de Netwerk Monitor van DD&M!") #GUI 
myscreen.refresh() #Refresh GUI
myscreen.getch()

curses.endwin() 

