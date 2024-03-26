import src.screen_handler as screen_handler
import src.PartCosts as PartCosts
import time


engine_builders = {}

screen_handler.add_text(engine_builders, "CHOOSE YOUR ENGINE" ,44, 0)

screen_handler.get_assets(engine_builders,"src/assets/EngineManus/ferrari.txt", 15,8)
screen_handler.get_assets(engine_builders, "src/assets/EngineManus/honda.txt", 76,10)
screen_handler.get_assets(engine_builders, "src/assets/EngineManus/mercedes.txt", 145,8)

screen_handler.add_text(engine_builders, "FERRARI" , 6, 27)
screen_handler.add_text(engine_builders, "HONDA" ,80, 27) 
screen_handler.add_text(engine_builders, "MERCEDES" ,140, 27)

screen_handler.add_text(engine_builders, "$" + (PartCosts.Ferrari), 27, 33, font_name='Rotated')
screen_handler.add_text(engine_builders, "$" +(PartCosts.Honda), 95, 33, font_name='Rotated')
screen_handler.add_text(engine_builders, "$" + (PartCosts.Mercedes), 167, 33, font_name='Rotated')



show_controls = {}
screen_handler.add_text(show_controls, "1          2          3 ", 30,10, font_name= "Doh")

screen_handler.add_text(show_controls, "GAME CONTROLS", 35,0, font_name= "Star Strips")

screen_handler.add_text(show_controls, "Try to stay under the cost cap, or else...", 15,30, font_name= "small")


def build_car(stdscr):
    while True:
        stdscr.clear()
        screen_handler.load_assets(engine_builders, stdscr)
        c = stdscr.getch()

        if c == ord('1'):
            break  # Exit the while loop

        if c == ord('2'):
            break

        if c == ord ('3'):
            break


def show_controls_screen(stdscr):    
    screen_handler.load_assets(show_controls, stdscr)
    stdscr.refresh()
    time.sleep(2.5)
 

