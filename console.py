import curses
from curses import wrapper 
import time


NUMBER_OF_CARS = 20

track=(r''' _ _ _ _ _ _ _ _ _ _ _ _
|                       \ 
|      _ _ _ _ _ _ _     \ 
|    |               \    \ 
|    |                \    \ 
|    |                 \    \ 
|    |                  \    \ 
|    |                   \    \ 
|    |                    \    \ 
 \    \                    \    \ 
  \    \                    \    \ 
   \    \                    \    \ 
    \    \                    \    \ 
     \    \                    \    \ 
      |    |                    \    \ 
      |    |                     \    \ 
       \    \                     \    \ 
        \    \                     \    \  
         |    |                     \    \ 
         |    |                      \    \ 
         |    |                       \    \ 
         |    |                        \    \ 
         |    |                         \    \ 
         |    |                         |     |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
         |    |                         |                                                                                 /
          \    \                        | _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _      /
           \    \                                                                                                  /    / 
            \    \                                                                                                /    /
             \    \                                                                                              /    /
              \    \                                                                                            /    /
               \    \                                                                                          /    /    
                \    \_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ /    / 
                 \                                                                                                /
                  \ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  / 
''')


def readFileIntoList(read_file):
  try:
    with open(read_file, 'r') as reader:
        database = [[char for char in line.strip()] for line in reader]
    return database      
  except IOError:
    print("File not accessible")
  except FileNotFoundError:
    print("File does not exist")


database = readFileIntoList("track_array.txt")





class racecar_class: 
    instances = []
    def __init__(self, current_position):
        self.current_position = current_position
        self.previous_position = None
            
    def get_next_position(self, grid,stdscr):
        stdscr.addstr(self.current_position[0],self.current_position[1], "🚗")
        
        rows = len(grid)
        cols = len(grid[0])
        
        # Define the direction of movement (left, up, right, down)
        self.directions = [(0, -2), (-1, 0), (0, 2), (1, 0), (1,1), (-1,-1), (1,-1), (-1,1)]
        
        # Iterate through all possible directions
        for self.direction in self.directions:
            next_row = self.current_position[0] + self.direction[0]
            next_col = self.current_position[1] + self.direction[1]
            
            # Check if the next position is within the grid boundaries
            if 0 <= next_row < rows and 0 <= next_col < cols:
                # Check if the next position is '2' and not equal to the previous position
                if grid[next_row][next_col] == '2' and (next_row, next_col) != self.previous_position:
                    self.previous_position = self.current_position
                    self.current_position = (next_row, next_col)








def main(stdscr):

    stdscr.nodelay(True)
    stdscr.leaveok(True)

    instances = []

    for i in range(1, NUMBER_OF_CARS*2-1,2):
        instances.append(racecar_class((32,105 - i*2-1)))
    
    while True:
        stdscr.refresh()
        stdscr.addstr(0,0, track)
        for i in instances:
            i.get_next_position(database, stdscr)

        time.sleep(.05)
        c = stdscr.getch()
        
        if c == ord('q'):
            break  # Exit the while loop


wrapper(main)