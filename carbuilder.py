import curses
from curses import wrapper 
import screen_handler

from art import text2art


asset_list = {}

screen_handler.add_text(asset_list, "CHOOSE YOUR ENGINE" ,48, 0, text2art)

screen_handler.get_assets(asset_list,"assets/EngineManus/ferrari.txt", 32,7)
screen_handler.get_assets(asset_list, "assets/EngineManus/honda.txt", 77,9)
screen_handler.get_assets(asset_list, "assets/EngineManus/mercedes.txt", 132,8)

screen_handler.add_text(asset_list, "FERRARI" , 25, 27, text2art)
screen_handler.add_text(asset_list, "HONDA" ,85, 27, text2art)
screen_handler.add_text(asset_list, "MERCEDES" ,132, 27, text2art)


def build_car(stdscr):
    
    screen_handler.load_assets(asset_list, stdscr)

    
    c = stdscr.getch()
    if c == ord('q'):
        pass  # Exit the while loop


wrapper(build_car)