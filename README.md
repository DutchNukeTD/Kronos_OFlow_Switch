# Kronos_OFlow_Switch
Adds costum button to easily switch between Kronos and OFlow node. Keeping the settings the same. 

## Install
1. Copy GB_Kronos to your .nuke folder.
2. Create a folder (example name: nodeCopys) and put there the kronos.nk and oflow.nk files. Everytime you call for the Kronos or Oflow node is called the adjusted file instead. 
3. Put the following in your menu.py file: 
import GB_Kronos
nukescripts.createOFlow = GB_Kronos.oflowNoX
nukescripts.createKronos = GB_Kronos.kronosNoX
