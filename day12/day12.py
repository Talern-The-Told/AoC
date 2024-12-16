file = r'day12\data.txt'

with open(file) as file:
    data = file.read()
    data = data.split('\n')



def surrounding_values(row,column,crop,plot,area,perimeter):
    print('Base is ',row,column)
    print('area is ',area,'perimeter is ',perimeter)
                
    area += 1
    print('add to area, now value is ',area)
    plot.append([row,column])
    
    front = row,column + 1, 
    back = row,column - 1
    up = row - 1,column
    down = row + 1,column

    for n_row,n_column in [front,back,up,down]: #looking at all surrounding values
        print('Looking at ',n_row,n_column)
        print('perimeter begins as ',perimeter)
        try:
            print('starting the try loop')
            if data[n_row][n_column] == crop and ([n_row,n_column]) not in plot and (n_row >-1 or n_column > -1):

                
                plot,area,perimeter = surrounding_values(n_row,n_column,crop,plot,area,perimeter)
            
            if data[n_row][n_column] != crop:
                perimeter += 1
                print('add to perimeter, perimeter is now ',perimeter)

                continue
            #if [row,column] in plot:
                #print(n_row,n_column, ' already included in plot')
        except:
            perimeter += 1
            print('out of range, perimeter is now ',perimeter)
            continue
        
        print('perimeter ends as ',perimeter)

        continue
        

    return plot,area,perimeter


crop_locations = []
done = []
cost = 0
for i,j in enumerate(data):
    for k,crop in enumerate(data[i]):
        if [i,k] not in done:
            print(i,k)
            done.append([i,k])
            area = 0
            perimeter = 0
            plot = []
            plot,area,perimeter = surrounding_values(i,k,crop,plot,area,perimeter)
            for spot in plot:
                done.append(spot)
            crop_locations.append([i,k,crop,area,perimeter, (area * perimeter)])
            cost += (area * perimeter)
        
    

for i in crop_locations:
    print(i)
print(cost)

#print(crop_locat'ions)



     
                



