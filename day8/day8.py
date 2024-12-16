#Find locations of antenna
from collections import defaultdict
import pandas as pd
import numpy as np
from itertools import permutations


file = r'day8\data.txt'

with open(file,'r') as file:
    data =file.read()

grid = data.splitlines()
n_columns = len(grid[0])+1
n_rows = len(grid)+1
coordinates = dict()
#grid = pd.DataFrame(list(row) for row in lines)

def boundary(set):
    bound = False
    if set[0] in range(0,n_rows):
        
        if set[1] in range(0,n_columns):
            
            bound = True
            return bound


for line in grid:

    for point in line:
        if point != '.':
            location = [grid.index(line),line.index(point)]
            location = list(location)
            
            if point in coordinates:

                coordinates[point] = coordinates[point] + [location]
                #print(f'adding to {point}')
                #print(type(coordinates[point]))
            
            else:
                coordinates[point] = [location]
                #print(coordinates[point])



point = 0
#print(coordinates)

antinode = []
for i in coordinates:

    perm = permutations(coordinates[i],2)
    for j,k in perm:

        rise = j[0]-k[0]
        run = j[1]-k[1]
        A1= ([j[0] + rise , j[1] + run])
        A2 = ([k[0] - rise , k[1] - run])
        print(j,k,rise,run)

        if boundary(A1):
            antinode.append(A1)
            #Part 2
            while boundary(A1):

                antinode.append(A1)
                print(f'A1{A1} - {rise,run}')
                A1 = ([A1[0] + rise , A1[1] + run])
                

        if boundary(A2):

            antinode.append(A2)
            #Part 2
            while boundary(A2):
                
                antinode.append(A2)
                print(f'A2{A2} - {rise,run}')
                A2 = ([A2[0] - rise , A2[1] - run])
                


#print((antinode))
print(len(antinode))
a = []
for i in antinode:
    if i not in a:
        a.append(i)
print(len(a))
#print(n_rows,n_columns)



#make pairs of antenna
#find slope between pairs
#Find location for antinodes
#Add location to unique list