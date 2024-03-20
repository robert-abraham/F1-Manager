from curses import wrapper 
import time
import screen_handler

#Import Assests 
track_array = screen_handler.readFileIntoList("assets/track_array.txt")
with open('assets/track_visual.txt', 'r') as file:
    track = file.read()
    file.close():



instances = []
NUMBER_OF_CARS = 20
for i in range(1, NUMBER_OF_CARS*2-1,2):
    instances.append(screen_handler.racecar_class((32,105 - i*2-1)))



def main(stdscr):
    stdscr.nodelay(True)
    stdscr.leaveok(True)
    while True:
        stdscr.refresh()
        time.sleep(.05)
        screen_handler.update_cars(stdscr, track,instances, track_array)
        c = stdscr.getch()
        
        if c == ord('q'):
            break  # Exit the while loop

wrapper(main)