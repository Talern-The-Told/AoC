import pandas as pd
import numpy as np
file = r'day6\day6data.txt'
with open(file,'r') as file:
    data =file.read()

lines = data.splitlines()

grid = pd.DataFrame(list(row) for row in lines)


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

def find_guard(grid):
    symbols = ['v','<','>','^']
    location = []
    for symbol in symbols:
        location = np.where(grid == symbol)
        if location[0].any(): #if there is any place where the symbol is found
            location = location[0].item(),location[1].item() #turn the location into integers
            return location,symbol

def find_straight_path(location,direction):
    path = []
    
    next_location = np.add(location,direction)

    next_area = grid[next_location[1]][next_location[0]]

    while next_area != '#':
        path_continues = True
        location = next_location
        if grid[location[1]][location[0]] != 'X':
            grid[location[1]][location[0]] = 'X'
            path.append(location)
        
        
        
        next_location = np.add(location,direction)
        try:
            next_area = grid[next_location[1]][next_location[0]]
        except:
            print('The guard has reached the end')
            path_continues = False
            break

        
       
        #print(f'The guard walks to {location}')
    print(f'The guard hit an obstacle at {next_location}')
    return location,path,path_continues

def turn_path(symbol):
    symbols = ['^','>','v','<']
    next_symbol_location = symbols.index(symbol) + 1
    if next_symbol_location == 4:
        next_symbol_location = 0
    next_symbol = symbols[next_symbol_location]
    return next_symbol

def total_path(grid):
    path = []
    location,symbol = find_guard(grid)
    path_continues = True
    count = 0
    while path_continues:
        direction = get_direction(symbol)
        #print(direction)

        location,straight_path,path_continues = find_straight_path(location,direction)

        symbol = turn_path(symbol)
        
        path.append(straight_path)
        count += len(straight_path)


    return grid,count,path



path_grid,path_count,path =total_path(grid)
print(path_count)
print(path_grid)







