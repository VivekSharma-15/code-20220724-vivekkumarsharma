import os
from os import sys
import json
from table1 import df

count = 0  
lst = []
j=0

#function to calculate bmi
def calc_bmi(height, weight):
    height_in_m = height/100
    bmi = round(weight/(height_in_m * height_in_m), 1)
    return bmi    

#function to add new column
def new_col(index):
    return({'BMI Category':df['BMI Category'][index], 'BMI':bmi, 'Health risk':df['Health risk'][index]})

#list of ranges
for range in df['BMI Range (kg/m2)']:    
    lst.append(float(range.split()[0]))

#sorted the list in reverse   
lst.sort(reverse=True)

# Opening JSON file
f = open(os.path.join(sys.path[0], "input.json"), "r")
   
# loading the json data
data = json.load(f)

# Iterating through the json
for record in data:
              
    #calculating bmi
    bmi = calc_bmi(record['HeightCm'], record['WeightKg'])
    
    #getting the max index of list
    index=len(lst)-1

    #checking for new records     
    if (len(record)) == 3:

        #add new columns
        for max_of_previous_range in lst:            
            
            #checking for all the ranges except the lowest
            if bmi >= max_of_previous_range:                    
                record.update(new_col(index))
                break
            
            #for the case where range is 18.4 and below
            if bmi<lst[index-1]:
                record.update(new_col(index))

            index=index-1

    #count overweight person        
    if 25<= bmi <= 29.9:
            count = count+1

print('total number of overweight: ', count)

#overwriting the json
with open(os.path.join(sys.path[0], "input.json"), "w") as outfile:
    json.dump(data, outfile)

# Closing file
f.close()