import src.Scenes.carbuilder as carbuilder
import src.Scenes.race as race
import src.Scenes.qualifying as qualifying
from curses import wrapper

#DISPLAY CONTROLS 
wrapper(carbuilder.show_controls_screen)

#TASK 1 - BUILD CAR
money_spent, CAR_CHOICES = wrapper(carbuilder.build_car) #Car Choices just returns user choices, it's used in qualifiying to display the drivers grid postion

#TASK 2 - QUALIFYING
results = wrapper(qualifying.qualifying, money_spent, CAR_CHOICES[3], CAR_CHOICES[4])

#TASK 3 - THE RACE
number_of_boosts = wrapper(race.animation)
print(number_of_boosts)
wrapper(race.result_screen, CAR_CHOICES[3], CAR_CHOICES[4], results, number_of_boosts)