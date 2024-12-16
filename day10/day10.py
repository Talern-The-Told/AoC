file = r'day10\data.txt'

with open(file) as file:
    data = file.read()
    data = data.split('\n')
  


  #Testing the modifitcations


    

def surrounding_values(row,column,value,score,top):


    front = row,column + 1, 
    back = row,column - 1
    up = row - 1,column
    down = row + 1,column

    for next in [front,back,up,down]: #looking at all surrounding values
        
        if next[0] < 0 or next[1] < 0:

            continue #if out of range, go to next value

        try: #if in range

            next_val = data[next[0]][next[1]]

            #print(temp_val,value)
            if int(next_val) == (int(value) + 1): #if the next value is more than current value
                    
                    #print(score)
                #print(next[0],next[1],next_val,'Keep going, score is ',score)
               
                score = surrounding_values(next[0],next[1],next_val,score,top) 
                #now set this next part of the path as the starting position to find the next step along the path
                
        except:
            continue    

        #Base case

    if int(value) == 9:
        
        #if ([row,column] not in top) is True: 

            #print("reached the top at ",row,column,value)
            #print("The score was ",score)
        score += 1
            #print("Now is where I would add to the score!",score)
            #top.append([row,column])

        #if ([row,column] in top):
            
            #print("You were already at ",row,column)
    return score        
                




trailheads = [] #all 0 locations
for i,j in enumerate(data):
    for k,m in enumerate(data[i]):
        if m == '0':
            trailheads.append([i,k,int(m)])
            
            

#print(trailheads)
sum = 0
for start in trailheads:
    top = []
    score = 0
    #print('\nTrailhead ',start)
    ToTheTop = surrounding_values(start[0],start[1],start[2],score,top)

    print(start,ToTheTop)
    sum += ToTheTop
    #break
    #print("Now onto next trailhead")
print(sum)
    