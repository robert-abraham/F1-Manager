"""
Robert
ICS3UO
main.py
June 14

Initalizes and handles all scenes 
"""

from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectButton import DirectButton
from direct.showbase.Loader import Loader
from Scenes.char_select import CharSelect
from Scenes.start_screen import StartScreen
from Scenes.main_menu import MainMenu
from Scenes.game import Game
from panda3d.core import loadPrcFileData
import sys
from stageflow import Flow
from stageflow import Stage


#Change resolution 
loadPrcFileData("", "win-size 1920  1080")

#make full screen 1470 x 956
loadPrcFileData("", "fullscreen t")
loadPrcFileData("", "textures-power-2 none")



ShowBase()
#An array used to indicate which countries have been conquered, since game hasnt started all are false
base.owned_countries = [False, False, False, False, False, False, False]
base.alive_emperors = ['Alexander', "Peter", "Seondak", "Pericies", "Qin", "Trajan", "Saladin"]

#screen res
base.resx = 1920
base.resy = 1080

#Image scaling, typically I used 2 for 1920x1080
base.scalebg = 2

#initilize the scene flower library, and add the 4 different stages
base.flow = Flow()
base.flow.add_stage('StartScrn', StartScreen())
base.flow.add_stage('CharSelcions', CharSelect())
base.flow.add_stage('MainMenu', MainMenu())
base.flow.add_stage('MainGame', Game())

#transtion to the first stage, being start screen
base.flow.transition('StartScrn') 

#initilize window
base.run()
