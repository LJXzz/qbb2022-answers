#1. 
```
#!/usr/bin/env python3

import sys  #import sys package

def parse_bed(fname): #define a function to read the bed file
    try:
        fs = open(fname, 'r')  #if we can find the file, just open and read it
    except:
        raise FileNotFoundError("That file doesn’t appear to exist") # if we can't find the file, just give a error information
    bed = [] # define a list
    wrong=0 # define a variables to count the amount of incorrectly-formatted line
   
    field_types = [str, int, int, str, float, str]  #a list with the type function
    for i, line in enumerate(fs):   #look through each line in the file
        if line.startswith("#"):    # if the line begins with #, never worry about it
            continue
        fields = line.rstrip().split()  #make every line a list and store it in fields
        fieldN = len(fields)  #calculate how many lines
        
        if fieldN < 3: # formate less than 3 is prohibited
            print(f"Line {i} appears malformed", file=sys.stderr)
            wrong=wrong+1 #count if there is a incorrectly-formatted line
        if fieldN == 10: #bed10 formatting is prohibited
            print(f"Line {i} appears malformed", file=sys.stderr)
            wrong=wrong+1 #count if there is a incorrectly-formatted line
        if fieldN == 11: #bed10 formatting is prohibited
            print(f"Line {i} appears malformed", file=sys.stderr)
            wrong=wrong+1 #count if there is a incorrectly-formatted line
        
################################################################################
In the above block of code, you are noting which lines are improperly formatted,
which is correct. However, because you don't have anything stopping the code
from continuing, it will continue on to execute the code below.
################################################################################

        split8 = fields[8].split(',') #split the RGB num into list
        for k in split8: 
            k=int(k) # make sure that itemRGB entries are all intgers
        
################################################################################
This properly splits the itemRGB field and will convert each element to an int.
But you are not saving the converted values anywhere so the changes you are
making will be lost and fields[8] will stay a string. You could either create
a list, put the integers into it, and then put that list into fields[8]. 
Alternatively, you could do each of the changes in place:

fields[8] = fields[8].split(',')
for k in range(len(fields[8])):
    fields[8][k] = int(fields[8][k])
################################################################################
       
        fields[10] = fields[10].strip(',').split(',') #delet the last comma for blockSize and make the string a list
        if len(fields[10]) != int(fields[9]) : # compare if the amount of blockSize is equal to blockCount
            print(f"Line {i} appears malformed", file=sys.stderr)
            wrong=wrong+1 #count if there is a incorrectly-formatted line
            
            continue
            
        fields[11] = fields[11].strip(',').split(',') #delet the last comma for blockStarts and make the string a list
        if len(fields[11]) != int(fields[9]) : # compare if the amount of blockStarts is equal to blockCount
            print(f"Line {i} appears malformed", file=sys.stderr)
            wrong=wrong+1 #count if there is a incorrectly-formatted line
        
            continue

################################################################################
These two blocks work well. The only thing I would suggest is converting
fields[9] into an int first (it never does get saved as an int). Then you can
do you list length checks against fields[9] without needing to convert it each
time. Also, you don't check the length of the list "fields", which means that
if you load a bed file with fewer columns, you will get an index out of range
error. So for fields[8:12], you need something like:

if fieldsN >= 8: # For itemRGB
################################################################################

        
        try:
            for j in range(min(len(field_types), len(fields))):
                fields[j] = field_types[j](fields[j])
            bed.append(fields)
        
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
            wrong=wrong+1 #count if there is a incorrectly-formatted line
            
        
    
    
    print('The amount of incorrectly-formatted line is '+ str(wrong)) # print out the amount of incorrectly-formatted line
        
    fs.close()
    return bed
    

    if __name__ == "__main__":
        fname = sys.argv[1]
        bed = parse_bed(fname)

################################################################################
Overall, this looks good. It needs a few tweaks but the basic logic is right.
The only other thing that is missing is converting fields[6] and fields[7] into
integers. This would be easy to do by adding two more items into the
field_types list at the top.
################################################################################

```







#2. 

To find the median, we just need to import statistics module and then use the median function

The number of malformed entries within the test data bed file: 3

The median number of exons for genes within the test data bed file: 4

################################################################################
Both of these are correct. However, next time you need to also include the
script you used to do the analysis (showing your work). That way you can get
more usefult feedback.
################################################################################

