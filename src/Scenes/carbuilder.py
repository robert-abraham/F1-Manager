import src.screen_handler as screen_handler
import src.PartCosts as PartCosts
import time


#USAGE EXAMPLE screen_handler.get_assets(asset_list, PATH, x, y)
#ALL THIS CODE MAY SEEM REPEATITIVE, EACH OF THESE SYMOOLIZES AN ASSET ON SCREEN, ALL ITS DOING IS ADDING TO A LIST, AND THAT LIST WILL LOAD ALL OF THE ASSETS WITHIN THE LIST
technical_director = {} #An example of a list, each list usually means a different scene. 
director_choices  = [("NEWEY",PartCosts.NEWEY), ("ALLISON", PartCosts.ALLISON), ("CARDILE",PartCosts.CARDILE)]

screen_handler.add_text(technical_director, "TECHNICAL        DIRECTOR" ,28, 0)
screen_handler.get_assets(technical_director,"src/assets/people.txt", 30,10)
screen_handler.add_text(technical_director, "NEWEY                    ALLISON                 CARDILE" , 32, 28, font_name="small")
screen_handler.add_text(technical_director, "$" + (PartCosts.NEWEY), 40, 33, font_name='Rotated')
screen_handler.add_text(technical_director, "$" +(PartCosts.ALLISON), 98, 33, font_name='Rotated')
screen_handler.add_text(technical_director, "$" + (PartCosts.CARDILE), 157, 33, font_name='Rotated')


primary_driver = {}
driver1_choices  = [("VERSTAPPEN",PartCosts.VERSTAPPEN), ("LECLERC", PartCosts.LECLERC), ("HAMILTON",PartCosts.HAMILTON)]

screen_handler.add_text(primary_driver, "PRIMARY       DRIVER" ,55, 0)
screen_handler.get_assets(primary_driver,"src/assets/people.txt", 30,10)
screen_handler.add_text(primary_driver, "VERSTAPPEN          LECLERC           HAMILTON" , 20, 28, font_name="small")
screen_handler.add_text(primary_driver, "$" + (PartCosts.VERSTAPPEN), 40, 33, font_name='Rotated')
screen_handler.add_text(primary_driver, "$" +(PartCosts.LECLERC), 98, 33, font_name='Rotated')
screen_handler.add_text(primary_driver, "$" + (PartCosts.HAMILTON), 157, 33, font_name='Rotated')

secondary_driver = {}
driver2_choices  = [("PIASTRI",PartCosts.PIASTRI), ("GASLY", PartCosts.GASLY), ("ALBON",PartCosts.ALBON)]

screen_handler.add_text(secondary_driver, "SECONDARY       DRIVER" ,40, 0)
screen_handler.get_assets(secondary_driver,"src/assets/people.txt", 29,10)
screen_handler.add_text(secondary_driver, "PIASTRI                     GASLY                           ALBON" , 29, 28, font_name="small")
screen_handler.add_text(secondary_driver, "$" + (PartCosts.PIASTRI), 40, 33, font_name='Rotated')
screen_handler.add_text(secondary_driver, "$" +(PartCosts.GASLY), 98, 33, font_name='Rotated')
screen_handler.add_text(secondary_driver, "$" + (PartCosts.ALBON), 157, 33, font_name='Rotated')

aerodynamic_focus = {}
aero_choices  = [("Front Wing",PartCosts.FrontWing), ("Rear Wing", PartCosts.RearWing), ("Air Intake",PartCosts.AirIntake)]
screen_handler.add_text(aerodynamic_focus, "AERODYNAMIC        FOCUS" ,32, 0)
screen_handler.get_assets(aerodynamic_focus,"src/assets/aerodynamic.txt", 10,10)
screen_handler.add_text(aerodynamic_focus, "FRONT WING           REAR    WING             AIR    INTAKE" , 10, 28, font_name="small")
screen_handler.add_text(aerodynamic_focus, "$" + (PartCosts.FrontWing), 27, 33, font_name='Rotated')
screen_handler.add_text(aerodynamic_focus, "$" +(PartCosts.RearWing), 95, 33, font_name='Rotated')
screen_handler.add_text(aerodynamic_focus, "$" + (PartCosts.AirIntake), 167, 33, font_name='Rotated')

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


cost_cap = "120,000,000" #Cost Cap For Car Building

CAR_CHOICES = [] 

#Car Choices Takes in a list of choices and gets a user input, it takes the input that correlates with the choice and adds it to a list, it also adds the cost of the choice to a variable named money_spent
def get_choice(stdscr, choices, money_spent):
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
    return money_spent

def build_car(stdscr, ):
    money_spent = 0
    #loading each set of choices, very hard to cut down this code, as the libary im using for some reason returns weird responses. I'd have to rewrite the screen handler module, which I  dont have time for. 
    stdscr.clear()
    stdscr.addstr("{:,}/{}".format(money_spent, cost_cap))
    screen_handler.load_assets(engine_builders, stdscr)
    money_spent = get_choice(stdscr, engine_choices,money_spent)
    
    stdscr.clear()
    stdscr.addstr("{:,}/{}".format(money_spent, cost_cap))
    screen_handler.load_assets(aerodynamic_focus, stdscr)
    money_spent = get_choice(stdscr, aero_choices,money_spent)

    stdscr.clear()
    stdscr.addstr("{:,}/{}".format(money_spent, cost_cap))
    screen_handler.load_assets(technical_director, stdscr)
    money_spent = get_choice(stdscr, director_choices,money_spent)


    stdscr.clear()
    stdscr.addstr("{:,}/{}".format(money_spent, cost_cap))
    screen_handler.load_assets(primary_driver, stdscr)
    money_spent = get_choice(stdscr, driver1_choices,money_spent)

    stdscr.clear()
    stdscr.addstr("{:,}/{}".format(money_spent, cost_cap))
    screen_handler.load_assets(secondary_driver, stdscr)
    money_spent = get_choice(stdscr, driver2_choices,money_spent)
    return money_spent, CAR_CHOICES


#This scene just shows the controls for choosing your car, only stays up for 3 seconds
def show_controls_screen(stdscr):    
    screen_handler.load_assets(show_controls, stdscr)
    stdscr.refresh()
    time.sleep(3)
 

