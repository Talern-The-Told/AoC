
import re
test="000000000000000000do()111111111111111111don't()22222222222don't()333333333333333do()444444444444444do()5555555"
file_path = r"C:\Users\tanne\OneDrive\Documents\GitHub\AdventOfCode\day3\data3.txt"
with open(file_path, "r") as data:
    corrupted_data = data.read()


value = 0
total = 0
total_dont = 0

def multiply(equation):
    multiples=[]
    multiples = re.findall(r'\d+',equation)
    multiples = [int(x) for x in multiples]
    value = multiples[0] * multiples[1]
    
    return value

#first remove all returns in the data, so its all one big text.
compiled_data=(re.sub('\n','', corrupted_data))

#I also have to end a do() at the very end because of how I find the don't information

compiled_data=  compiled_data +'do()'

#Then find all the information after don't and before do

regex_dont = r"don't[(][)].+?do[(][)]"

#Then remove all don't information

do_data=(re.sub(regex_dont,'', compiled_data))

#do_data is now has all data that either started with nothing or was preceded by do()


regex = (r"mul[(]\d\d?\d?,\d\d?\d?[)]")
mul = []

mul=list((re.findall(regex, do_data)))
#print(mul)




for equation in range(len(mul)):
    #print(mul[equation])
    value = multiply(mul[equation])
    #print(value)
    total += value
    #print(total)

#print(do_data)
print(total)