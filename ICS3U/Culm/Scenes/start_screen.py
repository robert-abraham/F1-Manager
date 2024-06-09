#from direct.showbase.ShowBase import ShowBase
import sys
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectButton import DirectButton
from direct.showbase.Loader import Loader
from direct.actor.Actor import Loader as loader
from stageflow import Stage
from stageflow.panda3d import Cutscene
from stageflow.prefab import Quit


class StartScreen(Stage):
    def enter(self, data):
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
        self.startscreen = \
            OnscreenImage(
                image="assets/StartScreenIMG2.png",
                parent=base.pixel2d,
                scale=(1920/base.scalebg, 0, 1080/base.scalebg),  # Image size
                pos=(base.resx/2, 1, -base.resy/2),  # Window size
            )
            
        self.startscreen.setBin("background",0)
        self.entities = [self.startbutton, self.startscreen]
        base.accept("escape", sys.exit)  # Escape quits
        

    def exit(self,data):
        for entity in self.entities:
            entity.destroy()
        return data

    def exit_call(self):
        base.flow.transition('CharSelcions') 