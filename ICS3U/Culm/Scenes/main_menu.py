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
from panda3d.core import TransparencyAttrib


class MainMenu(Stage):
    def enter(self, d):
        # Owned Countries in this order: AFR, ANT, AUS, EUR, IND, NOA, SOA
        self.owned_countries = [1,1,1,1,0,0,0]
        self.country_codes = ["AFR", "ANT", "AUS", "EUR", "IND", "NOA", "SOA"]
        self.countries_map = [0,0,0,0,0,0,0]
        self.imgMAP = \
            OnscreenImage(
                image="assets/Map/MAP.png",
                parent=base.pixel2d,
                scale=(897/base.scalebg, 0, 1003/base.scalebg),  # Image size
                pos=(base.resx/2, 1, -base.resy/2),  # Window size
            )
        self.imgMAP.setBin("background",0)
        base.accept("escape", sys.exit)  # Escape quits

        self.coloured_countries()

    def coloured_countries(self):
        for country_num ,country in enumerate(self.owned_countries):
            if country == True:
                print("dickhead", self.country_codes[country_num], country)
                self.countries_map[country_num]= \
                    OnscreenImage(
                        image=f"assets/Map/{self.country_codes[country_num]}.png",
                        parent=base.pixel2d,
                        scale=(897/base.scalebg, 0, 1003/base.scalebg),  # Image size
                        pos=(base.resx/2, 1, -base.resy/2),  # Window size
                        
                    )
                self.countries_map[country_num].setTransparency(TransparencyAttrib.MAlpha)

            
       
    def exit(self,data):
        for entity in self.entities:
            entity.destroy()
        return data

    def exit_call(self):
        base.flow.transition('') 