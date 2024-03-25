import curses
from curses import wrapper 
import screen_handler

from art import text2art
import math

#SETTINGS
NUMBER_OF_CARS = 20
REFRESH_RATE = 50

#ASSET IMPORT 
#USAGE EXAMPLE screen_handler.get_assets(asset_list, PATH, x, y)

asset_list = {}
track_array = screen_handler.readFileIntoList("assets/track_array.txt")
track = screen_handler.get_assets(asset_list, "assets/track_visual.txt", 0,0)
logo = screen_handler.get_assets(asset_list, "assets/f1_logo.txt", 54,5)
instances = screen_handler.load_cars(NUMBER_OF_CARS)


def main(stdscr):
    lap = 0
    start = None
    stdscr.nodelay(True)

    while True:
        screen_handler.load_assets(asset_list, stdscr)
        screen_handler.update_cars(stdscr ,instances, track_array)
        start, lap = screen_handler.update_lap(stdscr, text2art, math, asset_list, lap, start, 60, 17)
        stdscr.move(30,0)
        stdscr.refresh()        

        curses.napms(REFRESH_RATE)
        c = stdscr.getch()
        if c == ord('q'):
            break  # Exit the while loop

wrapper(main)