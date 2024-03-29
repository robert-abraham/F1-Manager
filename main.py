import src.Scenes.carbuilder as carbuilder
import src.Scenes.animation as animation
import src.Scenes.qualifying as qualifying
from curses import wrapper


wrapper(carbuilder.show_controls_screen)
money_spent, CAR_CHOICES = wrapper(carbuilder.build_car)

wrapper(qualifying.qualifying, money_spent, CAR_CHOICES[3], CAR_CHOICES[4])

wrapper(animation.animation)