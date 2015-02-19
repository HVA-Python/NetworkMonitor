#!/usr/bin/env python3

__author__ = "grasskill"
__date__ = "$Feb 19, 2015 12:22:11 PM$"

from dennisE import menu


title = "Press 'q' to exit "
updateFunction = None
x = None

def monitorclient():
    print("Monitoring")
    
setHost = None
setPort = None
Null = None


mainMenu = menu.Menu(title,update=updateFunction)

mainMenu.submenu = menu.Menu(title,update=updateFunction)

options = [{"name":"firstOption","function":Null},
           {"name":"secondOption","function":Null},
           {"name":"thirdOption","function":Null}]
mainMenu.addOptions(options)

mainMenu.explicit()
options = [{"name":"Monitor","function":monitorclient},
           {"name":"Hostname / IP address","function":setHost},
           {"name":"Set port","function":setPort}
           ]
mainMenu.addOptions(options)

mainMenu.clearOptions()

#mainMenu.implicit()
#options = [("firstOption",firstFunc),
#           ("secondOption",secondFunc),
#           ("thirdOption",thirdFunc)]
mainMenu.addOptions(options)



mainMenu.open()

