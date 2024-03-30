import curses
import time
import src.screen_handler as screen_handler

#SETTINGS
NUMBER_OF_CARS = 20
REFRESH_RATE = 25

#ASSET IMPORT 
#USAGE EXAMPLE screen_handler.get_assets(asset_list, PATH, x, y)

asset_list = {}
track_array = screen_handler.readFileIntoList("src/assets/track_array.txt")
track = screen_handler.get_assets(asset_list, "src/assets/track_visual.txt", 0,0)
logo = screen_handler.get_assets(asset_list, "src/assets/f1_logo.txt", 54,5)
instances = screen_handler.load_cars(NUMBER_OF_CARS)

def animation(stdscr):
    lap = 0
    start = None
    stdscr.nodelay(True)
    stdscr.clear()

    postion_of_bar_x= 170
    x_position = postion_of_bar_x+1
    direction = 1
    number_of_boosts = 0 

    while True:
        screen_handler.load_assets(asset_list, stdscr)
        screen_handler.update_cars(stdscr ,instances, track_array)
        start, lap = screen_handler.update_lap(stdscr, asset_list, lap, start, 60, 17)
        stdscr.move(30,0)
        stdscr.addstr(10, postion_of_bar_x, "|---------------|-------------|")
        stdscr.addstr(11, postion_of_bar_x, "Press Space To Trigger A Stop")
        stdscr.addstr(10, x_position, "X")
        x_position += direction
        if x_position <= postion_of_bar_x+1 or x_position >= postion_of_bar_x+ 28:
            direction *= -1
        stdscr.refresh()   
        curses.napms(REFRESH_RATE)
        c = stdscr.getch()
        if c == ord('q'):
            break  # Exit the while loop
        if c == ord(' '):
            if x_position == postion_of_bar_x+17:
                boost_identifer = {}
                screen_handler.add_text(boost_identifer, "BOOST!!!" ,160, 28)
                screen_handler.load_assets(boost_identifer, stdscr)
                stdscr.refresh()   
                time.sleep(1)
                number_of_boosts  +=1
        if lap == 5*20:
            break
    return number_of_boosts


race_results = {}
screen_handler.add_text(race_results, "THE    RESULTS    ARE    IN..." ,25, 0)
screen_handler.add_text(race_results, "PRESS ANY KEY TO CONTINUE", 90, 34, font_name='Rotated')


def result_screen(stdscr, driver1, driver2, results, number_of_boosts):
    stdscr.nodelay(False)   
    stdscr.clear()
    screen_handler.add_text(race_results, "{}      PLACED:     {}".format(driver1, int(results[0])- number_of_boosts), 3,7)
    screen_handler.add_text(race_results, "{}      PLACED:     {}".format(driver2, int(results[1])- number_of_boosts), 3,14)
    screen_handler.load_assets(race_results, stdscr)

    stdscr.getch()


