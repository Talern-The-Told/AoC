
import statistics as st #to find the median of a list
import pandas as pd

path = r"day5\day5data.txt"
rules = []
updates = []
success_counter = 0
median_sum = 0
while_counter = 0
updated_sets_median_sum = 0

with open(path) as file:
    for line in file:
        
        if line == '\n':
            for line in file:
                updates.append(line.strip())
            break
        rules.append(line.strip().split('|'))
        
        
rules = pd.DataFrame(rules, columns = ['X','Y'])
updates = pd.DataFrame(updates,columns = ['Update'])

in_order = False

#First, check if its in order


for set in updates["Update"]:
    #print('first for loop')
    #Turn the set into a list of integers
    set = list(set.split(','))  
    set = [int(word) for word in set]
    
    #find the median value

    
    was_updated = False
    row = 0

    while row < len(rules.index):

        
       

        #Now I define the X and Y value for this specific rule
        x = int(rules.iloc[row,0])
        y = int(rules.iloc[row,1])
        #print(x,y)
#PART 2 ASPECT. Rearranging


            #print(set)
        if (x in set and 
                    y in set): #if X and Y are present in the set
            
            while_counter +=1
            
            #print(set.index(x),set.index(y))
            #print(x,y)

            if set.index(x) > set.index(y): #If X is before Y
                print(f'{set} has failed because {x} is after {y}')
                
                #print(set.index(y),(x))
                set.remove(x)
                set.insert(set.index(y),(x))
                print(f'{set} was adjusted')
                in_order = False
                was_updated = True
            else:
                in_order = True
                #The set contains X and Y, and are in order
        else:
            in_order = True
            #The set does not contain X and Y

        if in_order:
            row += 1 
            #go to the next rule
        else:
            row = 0 
            #start from the beginning
    
    median = int((len(set)-1)/2)
    median_value = set[median]
    
    if was_updated:
        median = int((len(set)-1)/2)
        median_value = set[median]
        updated_sets_median_sum += median_value
        print(f'The median is {median_value}\n')
        print(f'The updated sum so far is: {updated_sets_median_sum}')

    else:
        print(f'{set} is in the correct order')
        median_sum += median_value #add the median of the correct set to the median sum
        print(f'The median is {median_value}\n')
        (f'sum so far is: {median_sum}')

print(f'The sum of the medians from the correctly ordered updates is \n{median_sum}')
print(f'The sum of the medians from the updated updates is \n{updated_sets_median_sum}')


#Step 1
#read the update

#Step 2
#Iterate through every rule
    #Step 2A
    #Is X and Y is present?
    #Is X before Y?

#If True, find median
#sum up medians
