import src.Scenes.carbuilder as carbuilder
import src.Scenes.race as race
import src.Scenes.qualifying as qualifying
from curses import wrapper

#DISPLAY CONTROLS 
wrapper(carbuilder.show_controls_screen)

#TASK 1 - BUILD CAR
money_spent, CAR_CHOICES = wrapper(carbuilder.build_car) #Car Choices just returns user choices, it's used in qualifiying to display the drivers grid postion

#TASK 2 - QUALIFYING
wrapper(qualifying.qualifying, money_spent, CAR_CHOICES[3], CAR_CHOICES[4])

#TASK 3 - THE RACE
wrapper(race.animation)