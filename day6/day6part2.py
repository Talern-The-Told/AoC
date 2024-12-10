import pandas as pd
import numpy as np
file = r'day6\test.txt'
with open(file,'r') as file:
    data =file.read()
lines = data.splitlines()
grid = pd.DataFrame(list(row) for row in lines)

potential_obstacles = 0

def find_guard(grid):
    symbols = ['v','<','>','^']
    location = []
    for symbol in symbols:
        location = np.where(grid == symbol)
        if location[0].any(): #if there is any place where the symbol is found
            location = location[0].item(),location[1].item() #turn the location into integers
            return location,symbol

def get_direction(arrow):
    if arrow == '^':
        direction = [-1,0]
    if arrow == '>':
        direction = [0,1]
    if arrow == 'v':
        direction = [1,0]
    if arrow == '<':
        direction = [0,-1]

    row_add = direction[0]
    column_add = direction[1]
    return row_add, column_add

def find_straight_path(location,direction,symbol):
    potential_obstacles = 0
    

    path = []
    
    next_location = np.add(location,direction)

    next_area = grid[next_location[1]][next_location[0]]

    while next_area != '#':
        
        potential_obstacles_sub = new_obstacle(location,symbol) #Part 2, do every spot along the path
        potential_obstacles += potential_obstacles_sub

        path_continues = True
        location = next_location
        if (grid[location[1]][location[0]] == '|' or 
            grid[location[1]][location[0]] == '-'):
            grid[location[1]][location[0]] = '+'
            
        if (grid[location[1]][location[0]] == '.'):
            if direction[0] == 0:
                grid[location[1]][location[0]] = '-'
            if direction[1] == 0:
                grid[location[1]][location[0]] = '|'
        
            path.append(location)
        
        next_location = np.add(location,direction)
        try:
            next_area = grid[next_location[1]][next_location[0]]
        except:
            print('The guard has reached the end')
            path_continues = False
            break


    print(f'The guard hit an obstacle at {next_location}')
    grid[location[1]][location[0]] = '+'
    return location,path,path_continues,potential_obstacles

def turn_path(symbol):
    symbols = ['^','>','v','<']
    next_symbol_location = symbols.index(symbol) + 1
    if next_symbol_location == 4:
        next_symbol_location = 0
    next_symbol = symbols[next_symbol_location]
    return next_symbol

def total_path(grid):
    potential_obstacles = 0
    path = []
    location,symbol = find_guard(grid)
    print('The guard is at {location} in {symbol}')
    path_continues = True
    count = 0
    while path_continues:
        direction = get_direction(symbol)
        #print(direction)

        location,straight_path,path_continues,potential_obstacles_sub = find_straight_path(location,direction,symbol)
        potential_obstacles += potential_obstacles_sub
        symbol = turn_path(symbol)
        
        path.append(straight_path)
        count += len(straight_path)


    return grid,count,path,potential_obstacles

def new_obstacle(location,symbol):
    potential_obstacles_sub = 0
    #find if there is a path going to the right from wherre the guard is located and directed
    turn = turn_path(symbol)
    
    new_direction = get_direction(turn)
    
    original_direction = get_direction(symbol)

    beginning = np.add(location,original_direction)

    print(f'Starting at {beginning}')
    #First we turn the direction of the path 90 degrees to see what is to the right of the guard
    print(f'we are going {symbol}')
    print(f'Now we are going to look {turn}')


    location = np.add(beginning,new_direction)

    clear = True

    while clear: #until there are either no existing obstacles or the guard falls off the map


        try: 

            next_location = np.add(location,new_direction)
            character = grid[location[1]][location[0]]
            next_character = grid[next_location[1]][next_location[0]]
            print(f"is there a potential at {next_location}? \n The next characters are {character} and {next_character}")
            
            
            print(f'\n{character,next_character}')
            if (character == '+' and
                next_character == '#'):
                print(f'we found a potential object location at {beginning}')
                potential_obstacles += 1
                
                grid[beginning[1]][beginning[0]] = '0'
                clear == False
                break

            
        
            
            if character == '#':
                clear == False
                break

            

        except:
            clear == False
            print('Hit a side!')
            break

        location = next_location
        return potential_obstacles_sub 
        
        

path_grid,path_count,path,potential_obstacles =total_path(grid)
print(path_count)
print(path_grid)
print(potential_obstacles)






