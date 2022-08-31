#1. 
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
        
        split8 = fields[8].split(',') #split the RGB num into list
        for k in split8: 
            k=int(k) # make sure that itemRGB entries are all intgers
        
       
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







2. 
the number of malformed entries within the test data bed file: 3
the median number of exons for genes within the test data bed file: 4
