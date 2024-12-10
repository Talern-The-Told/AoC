from Day1 import data, List_1, List_2
similarity_total = 0

length_1 = range(len(List_1))
length_2 = range(len(List_2))

#length_1 = range(10)
#length_2 = range(10)
print(length_2)
for a in length_1:
    similarity_times = 0

    for x in length_2:
        if List_1[a] == List_2[x]:
            similarity_times = similarity_times + 1  
        
            

    similarity_subtotal = similarity_times * List_1[a]
    similarity_total = similarity_total + similarity_subtotal
    print(f'print {a} and {x} \n {List_1[a]} is similar to {similarity_times} items in list 2,\n resulting in a similarity subtotal of {similarity_subtotal}')
        
print(f'The total similarity score is {similarity_total}')
