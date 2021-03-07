#Define Plugin Information
bl_info = {
    "name":"RAD GUI Panel Example",
    "description":"Panel generated from the RAD GUI Library",
    "author":"Ilobmirt",
    "version":(2021,3,7),
    "blender":(2,82,0),
    "location":"View3D > UI",
    "support":"COMMUNITY",
    "category":"Object"
}

#Import Libraries
import bpy, os
from . import RADGUI
from . import CUSTOMCLASSES

#Do some global activities here like loading the JSON Panel File
CurrentFolder: str = os.path.dirname(__file__)
RADGUI.Factory.LoadJSON(os.path.join(CurrentFolder,"TestPanel.JSON"))
#RADGUI.RADGUI_FACTORY.LoadJSON(os.path.join(CurrentFolder,"TestPanel.JSON"))

def register():
    RADGUI.Factory.Register()
    #RADGUI.RADGUI_FACTORY.Register()

def unregister():
    RADGUI.Factory.Unregister()
    #RADGUI.RADGUI_FACTORY.Unregister()

if __name__ == "__main__":
    register()