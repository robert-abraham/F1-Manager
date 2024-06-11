from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectButton import DirectButton
from direct.showbase.Loader import Loader
from Scenes.char_select import CharSelect
from Scenes.start_screen import StartScreen
from Scenes.main_menu import MainMenu
from panda3d.core import loadPrcFileData
import sys
from stageflow import Flow
from stageflow import Stage


#Change resolution 
loadPrcFileData("", "win-size 1920  1080")
#make full screen1470 x 956

loadPrcFileData("", "fullscreen t")
loadPrcFileData("", "textures-power-2 none")



ShowBase()


base.resx = 1920
base.resy = 1080
base.scalebg = 2

base.flow = Flow()
base.flow.add_stage('StartScrn', StartScreen())
base.flow.add_stage('CharSelcions', CharSelect())
base.flow.add_stage('MainMenu', MainMenu())
base.flow.transition('MainMenu') 

base.run()
