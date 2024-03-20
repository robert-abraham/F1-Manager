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


def find_valid_paths(track):
    valid_paths = []
    for i in range(len(track)):
        for j in range(len(track[i])):
            if track[i][j] == '2':
                valid_paths.append((i, j))
    return valid_paths

valid_paths = find_valid_paths(database)
print(valid_paths)





def readFileIntoList(read_file):

  try:
    with open(read_file, 'r') as reader:
        database = [[char for char in line.strip()] for line in reader]
       

    return database      
  except IOError:
    print("File not accessible")
  except FileNotFoundError:
    print("File does not exist")


database = readFileIntoList()


def find_valid_paths(track):
    valid_paths = []
    for i in range(len(track)):
        for j in range(len(track[i])):
            if track[i][j] == '2':
                valid_paths.append((i, j))
    return valid_paths

valid_paths = find_valid_paths(database)

def main(stdscr):
    stdscr.clear()
    #stdscr.addstr(0,0, track)
    stdscr.addstr(24,50, '🏎️')


    stdscr.refresh()
    stdscr.getch()


wrapper(main)