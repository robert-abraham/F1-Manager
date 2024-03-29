import src.screen_handler as screen_handler
from src.Scenes.carbuilder import cost_cap
import random



def determine_postion(stdscr, money_spent):
    grid_penalty = False
    if money_spent > int(cost_cap.replace(",", "")):
        grid_penalty = True
    pole_postion = random.randint(0, 9)
    print(pole_postion)
    c = stdscr.getch()
    while (True):
        if c == ord(str(pole_postion)):
            if grid_penalty == False:
                return (1,2), grid_penalty
            else:
                return (5,6), grid_penalty
        else: 
            if grid_penalty == False:
                return (5,6), grid_penalty
            else:
                return (9,10), grid_penalty
        


qualifying_scene = {}
screen_handler.add_text(qualifying_scene, "MONZA       F1       QUALIFYING" ,32, 0)
screen_handler.add_text(qualifying_scene, "THIS    WILL    DETERMINE    STARTING    POSTION" ,3, 10, font_name = 'small')
screen_handler.add_text(qualifying_scene, "CHOOSE    A    NUMBER    BETWEEN   0-9" ,30, 20, font_name = "small")
screen_handler.add_text(qualifying_scene, "YOUR    TEAM    WILL    ALSO    AFFECT    THIS" ,10, 29, font_name = 'small')

qualifying_results = {}
screen_handler.add_text(qualifying_results, "THE    RESULTS    ARE    IN..." ,25, 0)
screen_handler.add_text(qualifying_results, "PRESS ANY KEY TO CONTINUE", 90, 34, font_name='Rotated')


def qualifying(stdscr, money_spent, driver1, driver2):
    stdscr.clear()
    screen_handler.load_assets(qualifying_scene, stdscr)
    results, grid_penalty = determine_postion(stdscr, money_spent)
    stdscr.clear()
    if grid_penalty == True:
        screen_handler.add_text(qualifying_results, "COST    CAP    BREACH    DETECTED" ,35, 22, font_name = 'small')
        screen_handler.add_text(qualifying_results, "4    PLACE    GRID    PENALTY" ,42, 26, font_name = 'small')

    screen_handler.add_text(qualifying_results, "{}      PLACED:     {}".format(driver1, results[0]), 3,7)
    screen_handler.add_text(qualifying_results, "{}      PLACED:     {}".format(driver2, results[1]), 3,14)
    screen_handler.load_assets(qualifying_results, stdscr)

    stdscr.getch()