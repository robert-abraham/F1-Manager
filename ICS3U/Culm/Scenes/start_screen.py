"""
Robert
ICS3UO
start_screen.py
June 14

the start screen scene, just a basic scnene that has an image and a button
"""

import sys
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectButton import DirectButton
from direct.showbase.Loader import Loader
from stageflow import Stage


class StartScreen(Stage):
    #instead of __init__ its enter as the flow library handles classes differently
    def enter(self, data):
        
        #initilize a startbutton and its properties
        self.startbutton = DirectButton(
            relief = 1,
            pad = (0.5, 0.5),
            pos=(0,0,-0.7),
            scale = (0.1, 0.1, 0.1),
            text = 'Start',
            text_font = Loader.loadFont(self, 'assets/DroidSerif-Regular.ttf'),
            pressEffect=1,
            command = self.exit_call
        )

        #place a background image
        self.startscreen = \
            OnscreenImage(
                image="assets/StartScreenIMG2.png",
                parent=base.pixel2d,
                scale=(1920/base.scalebg, 0, 1080/base.scalebg),  # Image size
                pos=(base.resx/2, 1, -base.resy/2),  # Window size
            )
        #set rendering order so that the background renders before the button so that the button overlays the background
        self.startscreen.setBin("background",0)

        #a list of all entities in scene so they can be later destroyed
        self.entities = [self.startbutton, self.startscreen]

        #create a handler task that looks for the escape key to be cliked
        base.accept("escape", sys.exit)  # Escape quits
        

    # this function is automatically called by the flow library upon exiting the scene
    def exit(self,data):
        for entity in self.entities:
            entity.destroy()
        return data

    #call to transtion scene to the next scene
    def exit_call(self):
        base.flow.transition('CharSelcions') 