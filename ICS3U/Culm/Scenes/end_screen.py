"""
Robert
ICS3UO
start_screen.py
June 14

the start screen scene, just a basic scnene that has an image and a button
"""

import sys
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.Loader import Loader
from stageflow import Stage


class EndScreen(Stage):
    #instead of __init__ its enter as the flow library handles classes differently
    def enter(self, data):
        if data == True:
            #initilize a startbutton and its properties
            self.game_status  = \
                OnscreenText(
                    parent=base.a2dpBotCenter,
                    pos = (0,-0.2),
                    font= Loader.loadFont(self, 'assets/DroidSerif-Bold.ttf'),
                    scale=(0.1, 0.1, 0.1),
                    text=("Congrats on Winning!"),
                    fg = (255,255,255,1)
                )


        #place a background image
        self.endscreen = \
            OnscreenImage(
                image="assets/StartScreenIMG2.png",
                parent=base.pixel2d,
                scale=(1920/base.scalebg, 0, 1080/base.scalebg),  # Image size
                pos=(base.resx/2, 1, -base.resy/2),  # Window size
            )
        
        #set rendering order so that the background renders before the button so that the button overlays the background
        self.endscreen.setBin("fixed",10)
        self.game_status.setBin("fixed",11)

        #a list of all entities in scene so they can be later destroyed
        self.entities = [self.endscreen]

        #create a handler task that looks for the escape key to be cliked
        base.accept("escape", sys.exit)  # Escape quits
        
