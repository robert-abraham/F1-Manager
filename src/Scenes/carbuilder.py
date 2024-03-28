import src.screen_handler as screen_handler
import src.PartCosts as PartCosts
import time



aerodynamoc_focus = {}





engine_builders = {}
engine_choices  = [("Ferrari",PartCosts.Ferrari), ("Honda", PartCosts.Honda), ("Mercedes",PartCosts.Mercedes)]
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

money_spent =  0
cost_cap = "150,000,000"

CAR_CHOICES = []

def get_choice(stdscr, choices):
    global money_spent
    c = stdscr.getch()
    while (True):
        if c == ord('1'):
            CAR_CHOICES.append(choices[0][0])
            money_spent += int(choices[0][1].replace(",", ""))
            break
        if c == ord('2'):
            CAR_CHOICES.append(choices[1][0])
            money_spent += int(choices[1][1].replace(",", ""))
            break
        if c == ord ('3'):
            CAR_CHOICES.append(choices[2][0])
            money_spent += int(choices[2][1].replace(",", ""))
            break


def build_car(stdscr):
    stdscr.clear()
    stdscr.addstr("{:,}/{}".format(money_spent, cost_cap))
    screen_handler.load_assets(engine_builders, stdscr)
    get_choice(stdscr, engine_choices)



def show_controls_screen(stdscr):    
    screen_handler.load_assets(show_controls, stdscr)
    stdscr.refresh()
    time.sleep(2.5)
 

