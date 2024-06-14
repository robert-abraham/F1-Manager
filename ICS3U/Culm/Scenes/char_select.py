"""
Robert
ICS3UO
start_screen.py
June 14

the start screen scene, just a basic scene that has an image and a button
"""

from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectButton import DirectButton
from direct.showbase.Loader import Loader
import sys
from stageflow import Stage

from Scenes.owned_countries import claim_country


#list of all leaders that can be played, ands their countries
characters = ['Alexander', "Peter", "Seondak", "Pericies", "Qin", "Trajan", "Saladin", ]
countries = ["Macedonia","Russia", "Korea",'Greece', ' China',  'Rome', "Arabian"]

#placeholder value will be later used to determine which charachter you are hovering
current = 0 

class CharSelect(Stage):
    def enter(self, d):
        # display the first leader you can choose
        self.charselect = \
            OnscreenImage(
                image="assets/Leaders/Alexander.png",
                parent=base.pixel2d,
                scale=(1920/3, 0, 1080/3),  # Image size
                pos=(base.resx/2, 1, -base.resy/2),  # Window size
            )
        
        #a lock btn for when you want to choose your leader
        self.lockbtn = \
            DirectButton(
                relief = 1,
                pad = (0.5, 0.5),
                pos=(0,0,0.1),
                scale = (0.1, 0.1, 0.1),
                text = 'Lock In',
                text_font = Loader.loadFont(self, 'assets/DroidSerif-Regular.ttf'),
                pressEffect=1,
                parent=base.a2dBottomCenter,
                command = self.exit_call
            )

        #another background image
        self.background = \
            OnscreenImage(
                image="assets/Primbackground.png",
                parent=base.pixel2d,
                scale=(1920/base.scalebg, 0, 1080/base.scalebg),  # Image size
                pos=(base.resx/2, 1, -base.resy/2),  # Window size
            )
        
        #displays the which country the leader is from and which one out of seven you are currently hovering
        self.country_selection  = \
            OnscreenText(
                parent=base.a2dpTopCenter,
                pos = (0,-0.2),
                font= Loader.loadFont(self, 'assets/DroidSerif-Bold.ttf'),
                scale=(0.1, 0.1, 0.1),
                text=((countries[current]+ " - "+characters[current] +" ("+str(characters.index(characters[current])+1)+"/7)")),
                fg = (255,255,255,1)
            )

        # another entities list that describe all the entities in the scene
        self.entities = [self.background, self.lockbtn, self.charselect, self.country_selection]

        #setting the rendering order so that all entities render in the correct order
        self.charselect.setBin("opaque",0)
        self.background.setBin("background",0)

        #create a task that watchs for the a or the d button to be pressed if its pressed it scrolls to the next entitiy in the array
        base.accept('d', self.switch_image, [1])
        base.accept('a', self.switch_image, [-1])
        base.accept("escape", sys.exit)  # Escape quits

    #the function that gets called when A or D are pressed
    def switch_image(self,step):
        global current
        #handles any overflow issues so that the array cannot get out of index
        if (current+step > len(characters)-1):
            current = 0 
        
        #if not issues with overflowing switch to the next image
        else: 
            current += step

        #using the same entity except just changing its image property
        self.charselect.setImage(f"assets/Leaders/{characters[current]}.png")

        #again using the same entity just changging its text property to reflect on the new leaders properties
        self.country_selection.setText((countries[current]+ " - "+characters[current] +" ("+str(characters.index(characters[current])+1)+"/7)"))

    #automatically called upon switching the scene
    def exit(self, data):
        for entity in self.entities:
            entity.destroy()
        return data
    
    #call for an exit
    def exit_call(self):
        base.chosen_emperor = characters[current]

        #since you locked in a leader you get to claim your first land
        claim_country(characters[current],True)
        base.flow.transition('MainMenu') 