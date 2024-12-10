
import statistics as st #to find the median of a list
import pandas as pd

path = r"day5\day5data.txt"
rules = []
updates = []
success_counter = 0
median_sum = 0

with open(path) as file:
    for line in file:
        
        if line == '\n':
            for line in file:
                updates.append(line.strip())
            break
        rules.append(line.strip().split('|'))
        
        
rules = pd.DataFrame(rules, columns = ['X','Y'])
updates = pd.DataFrame(updates,columns = ['Update'])

for set in updates["Update"]:
    
    #Turn the set into a list of integers
    set = list(set.split(','))  
    set = [int(word) for word in set]
    
    #find the median value
    median = int((len(set)-1)/2)
    median_value = set[median]
    
    success = True
    
    for index, row in rules.iterrows():

        #Now I define the X and Y value for this specific rule
        x = int(row.iloc[0])
        y = int(row.iloc[1])



        if (x in set and 
            y in set): #if X and Y are presetn int the set

            if set.index(x) > set.index(y): #If X is before Y
                success = False #Then this is not in the correct order
                #print(f'{set} has failed because {x} is after {y}')
                

    if success: #If the set is in the correct order
        #print(f'{set} is in the correct order \n'
              #f'The median is {median_value} and the length is {len(set)}')

        median_sum += median_value #add the median of the correct set to the median sum
        #print(f'The median sum so far is: {median_sum}')

print(f'The sum of the medians from the correctly ordered updates is {median_sum}')



#Step 1
#read the update

#Step 2
#Iterate through every rule
    #Step 2A
    #Is X and Y is present?
    #Is X before Y?

#If True, find median
#sum up medians
