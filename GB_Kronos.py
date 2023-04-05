# Python 3
# 2023-01-12
# Golan version of Kronos for normal Nuke version - No X.
# Adds a user button to OFlow and Kronos node. 
# With the button you van switch between the two while keeping the settings the same. 


import nuke

def oflowNoX():
    nuke.nodePaste(r'C:/Users/The Compound PC 10/.nuke/nodeCopys/oflow.nk')

def kronosNoX():
    nuke.nodePaste(r'C:/Users/The Compound PC 10/.nuke/nodeCopys/kronos.nk')