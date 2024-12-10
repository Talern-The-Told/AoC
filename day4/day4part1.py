import numpy as np
import pandas as pd

data = []

with open(r"day4\day4.txt") as file:
    for line in file:
        
        #total_data = file.read()
        data.append(line.strip())
        
with open(r"day4\day4.txt") as file:
    total_data = file.read()


n_columns = len(data[0]) - 1 
n_rows = len(data) - 1 

def get_forward(data,row,column):
    word = ''
    while (0 <= row <= n_rows and 
           len(word) < 4 and 
           0 <= column <= n_columns):
        
        #print(column,row)

        word += str(data[row][column])
        column += 1
    #print(word)
    return word

def get_backward(data,row,column):
    word = ''
    while (0 <= row <= n_rows and 
           len(word) < 4 and 
           0 <= column <= n_columns):
        
        #print(column,row)

        word += str(data[row][column])
        column -= 1
    #print(word)
    return word

def get_down(data,row,column):
    word = ''
    while (0 <= row <= n_rows and 
           len(word) < 4 and 
           0 <= column <= n_columns):
        
        #print(column,row)
        
        word += str(data[row][column])
        row += 1
    #print(word)
    return word

def get_up(data,row,column):
    word = ''
    while (0 <= row <= n_rows and 
           len(word) < 4 and 
           0 <= column <= n_columns):
        
        #print(column,row)
        
        word += str(data[row][column])
        row -= 1
    
    return word

def get_down_right(data,row,column):
    word = ''
    while (0 <= row <= n_rows and 
           len(word) < 4 and 
           0 <= column <= n_columns):
        
        #print(column,row)
        
        word += str(data[row][column])
        row += 1
        column += 1
    #print(word)
    return word

def get_down_left(data,row,column):
    word = ''
    while (0 <= row <= n_rows and 
           len(word) < 4 and 
           0 <= column <= n_columns):  

        #print(column,row)
        
        word += str(data[row][column])
        row += 1
        column -= 1
    #print(word)
    return word

def get_up_left(data,row,column):
    word = ''
    while (0 <= row <= n_rows and 
           len(word) < 4 and 
           0 <= column <= n_columns):  

        #print(column,row)
        
        word += str(data[row][column])
        row -= 1
        column -= 1
    #print(word)
    return word

def get_up_right(data,row,column):
    word = ''
    while (0 <= row <= n_rows and 
           len(word) < 4 and 
           0 <= column <= n_columns):  

        #print(column,row)
        
        word += str(data[row][column])
        row -= 1
        column -= 1

    #print(word)
    return word

def get_x_positions(data):
    coordinates = []
    for row in range(n_rows+1):
        for column in range(n_columns+1):
            
            if data[row][column] == 'X':
                coordinates.append([row,column])    
    return coordinates

def get_surrounding_words(x_spots):
    
    surrounding_words = []

    for x in x_spots:
        
        forward = get_forward(data,x[0],x[1])
        backward = get_backward(data,x[0],x[1])
        upright = get_up_right(data,x[0],x[1])
        upleft = get_up_left(data,x[0],x[1])
        downright = get_down_right(data,x[0],x[1])
        downleft = get_down_left(data,x[0],x[1])
        up = get_up(data,x[0],x[1])
        down =  get_down(data,x[0],x[1])
        surrounding_words.append([
                                forward,
                                backward,
                                upright,
                                upleft,
                                downright,
                                downleft,
                                up,
                                down])
    return surrounding_words

def is_xmas(surrounding_words):
    xmas_score = 0
    
    for set in surrounding_words:
        for word in set:
            
            if word == "XMAS":
                xmas_score += 1
                print(word)
    return xmas_score


x = get_x_positions(data)
surrounding_words = get_surrounding_words(x)
x_added_up = 0
'''for word in surrounding_words:
    print(word,len(word))
    x_added_up +=1'''


score = is_xmas(surrounding_words)
x_count = total_data.count('X')
print(f"number of X coordinates we found surrounding words for: {x_added_up}")
print(f"number of X's:{x_count}\nnumber of X's found:{len(x)}")
#print(surrounding_words)
print(f'n_rows: {n_rows}')
print(f'n_columns: {n_columns}')      
print(f"{score} instances of XMAS")
