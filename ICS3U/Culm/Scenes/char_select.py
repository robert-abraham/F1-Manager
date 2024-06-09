from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectButton import DirectButton
from direct.showbase.Loader import Loader
import sys
from stageflow import Stage
from stageflow.panda3d import Cutscene



characters = ['Alexander', "Peter", "Seondak", "Pericies", "Qin", "Trajan", "Saladin", ]
countries = ["Macedonia","Russia", "Korea",'Greece', ' China',  'Rome', "Arabian"]
current = 0 

class CharSelect(Stage):
    def enter(self, d):
        self.charselect = \
            OnscreenImage(
                image="Assets/Alexander.png",
                parent=base.pixel2d,
                scale=(1920/3, 0, 1080/3),  # Image size
                pos=(1470/2, 1, -956/2),  # Window size
            )
        
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
            )

        self.background = \
            OnscreenImage(
                image="assets/Primbackground.png",
                parent=base.pixel2d,
                scale=(1920/base.scalebg, 0, 1080/base.scalebg),  # Image size
                pos=(base.resx/2, 1, -base.resy/2),  # Window size
            )
            
        self.country_selection  = \
            OnscreenText(
                parent=base.a2dpTopCenter,
                pos = (0,-0.2),
                font= Loader.loadFont(self, 'assets/DroidSerif-Bold.ttf'),
                scale=(0.1, 0.1, 0.1),
                text=((countries[current]+ " - "+characters[current] +" ("+str(characters.index(characters[current])+1)+"/7)")),
                fg = (255,255,255,1)

            )

        self.entities = [self.background, self.lockbtn, self.charselect, self.country_selection]


        self.charselect.setBin("opaque",0)
        self.background.setBin("background",0)

        base.accept('d', self.switch_image, [1])
        base.accept('a', self.switch_image, [-1])
        base.accept("escape", sys.exit)  # Escape quits

    def switch_image(self,step):
        global current
        if (current+step > len(characters)-1):
            current = 0 
        else: 
            current += step
        self.charselect.setImage(f"Assets/{characters[current]}.png")
        self.country_selection.setText((countries[current]+ " - "+characters[current] +" ("+str(characters.index(characters[current])+1)+"/7)"))

