from art import text2art
import math

def readFileIntoList(read_file):
  try:
    with open(read_file, 'r') as reader:
        database = [[char for char in line.strip()] for line in reader]
    return database      
  except IOError:
    print("File not accessible")
  except FileNotFoundError:
    print("File does not exist")

class racecar_class:     
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


def load_cars(NUMBER_OF_CARS):
  instances = []
  for i in range(1, NUMBER_OF_CARS*2+1,2):
      instances.append(racecar_class((32,105 - i*2-1)))
  
  return instances

def update_cars(stdscr, instances,track_array):
    for i in instances:
        i.get_next_position(track_array, stdscr)

def get_assets(asset_list, path, posx, posy):
    with open(path, 'r') as file:
        content = file.readlines()  # Read the entire contents of the file
        asset_list[path] = (content, posx, posy)

def add_text(asset_list, text ,x, y, font_name = "Big"):
  content = (text2art(text, font = font_name)).splitlines()
  asset_list[text] = (content, x, y)

def load_assets(assest_list: dict, stdscr):
  for file, contents in assest_list.items():
    asset, x , y = contents
    for a in asset:
      stdscr.addstr(y, x, a)
      y+=1

def update_lap(stdscr, asset_list, lap, start, x ,y):
  
  if start != None:
    if stdscr.instr(2,2) != start:
      lap+=1
  else: 
    start= stdscr.instr(2,2)

  lap_update_contents = (text2art("LAP {}/16".format(math.ceil(lap/20)))).splitlines()
  asset_list["LAP_UPDATER"] = (lap_update_contents, x, y)

  return start, lap