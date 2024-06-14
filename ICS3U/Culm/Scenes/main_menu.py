"""
Robert
ICS3UO
main_menu.py
June 14

the main menu scene, displays the map, and which countries you currently have colonised
"""

import sys
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectButton import DirectButton
from direct.showbase.Loader import Loader
from stageflow import Stage
from panda3d.core import TransparencyAttrib

class MainMenu(Stage):
    def enter(self, d):
        self.country_codes = ["AFR", "ANT", "AUS", "EUR", "IND", "NOA", "SOA"]
        #An array that holds the image objects, 0 is placeholder waiting to be filled
        self.countries_map = [0,0,0,0,0,0,0]
        #initilizes the map
        self.imgMAP = \
            OnscreenImage(
                image="assets/Map/MAP.png",
                parent=base.pixel2d,
                scale=(897/base.scalebg, 0, 1003/base.scalebg),  # Image size
                pos=(base.resx/1.5, 1, -base.resy/2),  # Window size
            )
        #sets the rendering order to be in the background
        self.imgMAP.setBin("background",1)

        #another handler that watches for the escape key
        base.accept("escape", sys.exit)  # Escape quits

        #calls function to "colour in" the colonised countries
        self.coloured_countries() 

        #a regular background behind the map
        self.background = \
            OnscreenImage(
                image="assets/Primbackground.png",
                parent=base.pixel2d,
                scale=(1920/base.scalebg, 0, 1080/base.scalebg),  # Image size
                pos=(base.resx/2, 1, -base.resy/2),  # Window size
            )
        
        #informing the user to click on a button to go to battle
        self.battle_indicator  = \
            OnscreenText(
                parent=base.a2dpTopCenter,
                pos = (0,-0.2),
                font= Loader.loadFont(self, 'assets/DroidSerif-Bold.ttf'),
                scale=(0.1, 0.1, 0.1),
                text=("Click On A Charachter to go to battle with!"),
                fg = (255,255,255,1)
            )

        #sets the background to be rendered first
        self.background.setBin("background",0)

        # an array storing the battle button entities
        self.battle_btns = []

        #iterate through the alive emperors and create a button for each of them
        if len(base.alive_emperors) == 0:
            base.flow.transition('StartScrn') 
        else:
            for count, emperor in enumerate(base.alive_emperors):
                self.battle_btns.append(DirectButton(
                    relief = 1,
                    pad = (0.5, 0.5),
                    pos=(-1.4, 0,  0.75 -(0.3*count)),
                    scale = (0.1, 0.1, 0.1),
                    text = emperor,
                    text_font = Loader.loadFont(self, 'assets/DroidSerif-Regular.ttf'),
                    pressEffect=1,
                    command = self.exit_call,
                    extraArgs = [emperor]


                ))

        self.entities = [self.background, self.battle_indicator, self.imgMAP]


    #when called it will look to fill in all colonised countries
    def coloured_countries(self):
        #iterate through the owned countries of the player
        for country_num ,country in enumerate(base.owned_countries):
            #if owned then create an image save that entity to an array, and overlay a replica of the country except in red
            if country == True:
                self.countries_map[country_num]= \
                    OnscreenImage(
                        image=f"assets/Map/{self.country_codes[country_num]}.png",
                        parent=base.pixel2d,
                        scale=(897/base.scalebg, 0, 1003/base.scalebg),  # Image size
                        pos=(base.resx/1.5, 1, -base.resy/2),  # Window size
                        
                    )
                #make sure the image is transparent so that the rest of the map shows up
                self.countries_map[country_num].setTransparency(TransparencyAttrib.MAlpha)

            
# destroy all entitites in the scene
    def exit(self,data):
        for entity in self.entities:
            entity.destroy()

        for entity in self.battle_btns:
            entity.destroy()

        for entity in self.countries_map:
            if type(entity) is not int:
                entity.destroy()
        return data

#when called begins the process of transitioning scenes
    def exit_call(self, emperor):
        base.flow.transition('MainGame', emperor) 
