#USAGE:  python scriptname.py input_filename [number_lines_to_display]
import sys #import module
filename = sys.argv[1] #SET input filename
if len(sys.argv) > 2: #IF user-specified number of lines provided
    n_lines = int(sys.argv[2]) #SET the desired number of lines
else：#OTHERWISE
    n_lines=10 #THEN we need to SET the desired number of displayed lines to a default

storage=[] #create a storage list for lines in the file

for i, line in enumerate(open(filename)): # FOR every line in the open file
    storage.append(line) #add the line to the storage list


subset=storage[-n_lines:]
# create a subset of the storage list to be the last n_lines items in the storage list

for i in subset: #for everyline in the subset
    print(i.strip('\r\n')) #print the line


# This looks great! It does exactly what it's supposed to and is very readable.
# Just a note is that you don't need to use enumerate when you read in the file
# since you don't use the line numbers at all, but it doesn't hurt anything.
# You seem to have a good grasp on what you're doing. So, keep it up! - Mike