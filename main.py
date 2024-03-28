import src.Scenes.carbuilder as carbuilder
import src.Scenes.animation as animation
from curses import wrapper


#wrapper(carbuilder.show_controls_screen)
wrapper(carbuilder.build_car)
#wrapper(animation.animation)