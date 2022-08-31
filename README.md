# QBB2022 - Day 2 - Homework Excercises Submission

1. 
    #!/usr/bin/env python3

    import sys #import sys package which allows us to read in the input from the terminal 

    def parse_vcf(fname):  # define a new function and it takes an argument called "fname"

    vcf = [] # set up a list called vcf to store vcf information
    info_description = {} # set up a dictionary called info_description
    info_type = {} # set up a dictionary called info_tyoe
    format_description = {} # set up a dictionary
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        }                  # allows us to use information from the header to tell python what types of data to expect
    malformed = 0   # initialize a variavle to count the number of malformed VCF lines

    #open the VCF file; if it doesn't work, tell the user
    try:
        fs = open(fname)
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr) #error message to user
    
    
    
    #block for the headlines 
    for h, line in enumerate(fs):  # look through everyline of the VCD file, keeping trak of the line number
        if line.startswith("#"): # for header line only
            try:
                if line.startswith("##FORMAT"):    #find the line start with ##FROMAT
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","  
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            elif name == "Type":
                                Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header")
        
        
        
        # block for processing the data
        else:
            try: # try to do all of this :
                #fields is a list that stores the info in one line of the VCF
                fields = line.rstrip().split("\t") #splits each line on a tab character, so that every column is an item in the list 'fields'
                fields[1] = int(fields[1]) # convert the SNP position into an integer(if this doesn't work, we'll automatically go to the except block)
                if fields[5] != ".": # if the QuAL column is not empty(i.e., it has a decimal in ti that represents the SNP quality)
                    fields[5] = float(fields[5]) # then forcibly convert it into a decimal
                info = {} # create a dictionary to store the information of info
                #we want the info dictionary to look like this: {"AC":91, "AN":5096, ...}
                for entry in fields[7].split(";"): # the list looks like : ["AC=91","AN=5096".....]
                # the first entry we're working with if "AC=91"
                    temp = entry.split("=") # temp is a list. if we are working with "AC=91", then the temp is ["AC","91"]
                    if len(temp) == 1: # if there is only one element in the temp list 
                        info[temp[0]] = None #temp[0] is "AC" . we are adding "AC" to the dictionary and we give the value"none" to this key
                    else: # otehrwise, the infro field is not empty and we are good 
                        name, value = temp #temp = ['AC','91'] and name = "AC", value = "91"
                        #in these next two lines, we are converting the data in each entry to its correct data type. This data type was sepcified in the header section that we parsed above
                        Type = info_type[name] # Here we are geting the python function for data type conversion that corresponds to what the entry should be.
                        #Ex: Type = info_type['AC'], info_type is a dictionary we made in the header parsing section that tells us what data type that entry should be.
                        info[name] = type_map[Type](value) # here we are geting the python function for converting the enty to the corrct data type
                        #Ex: For AC: info["AC"]= type_map["Integer"]("91"), info["AC"]=intefer 91
                
                fields[7] = info # replace the 8th item of the "fields" list with the info dictionary taht we just made
                if len(fields) > 8: # if we still have more columns after the INFO column, then we still have more stuff to do
                    fields[8] = fields[8].split(":") # Ex for field[8] in a general way: GT:DP:AF:BG:RU, this line spliting the FORMAT column by":"
                    if len(fields[8]) > 1: # If there is multiple format column, we have to deal with all of them individually
                        for i in range(9, len(fields)): # this goes through all the columns after the format column for us 
                            fields[i] = fields[i].split(':') # split each columnalong a ":"  
                    else: # if the genotypes don't have more than one value in the item
                        fields[8] = fields[8][0] #E.X. fields[8] is ['GT']. This line just makes fields[8]="GT". We set the value of fields[8] to be "GT"
                vcf.append(fields) # we've finished reformating/cleaning all the columns; now we add this line to our VCF list. Th list is 
            
            except:# if anything in the try block falls, then 
                malformed += 1 #increment the "malformed" variable by 1
                
    vcf[0][7] = info_description
    if len(vcf[0]) > 8:
        vcf[0][8] = format_description
    if malformed > 0:
        print(f"There were {malformed} malformed entries", file=sys.stderr)
    return vcf

    if __name__ == "__main__":
    	fname = sys.argv[1]
    	vcf = parse_vcf(fname)
    	for i in range(10):
	    print(vcf[i])
	   





2. 
	from vcfParser import parse_vcf #import the parse_vcf function from previous python document

	import sys
	Rname = sys.argv[1]
	dbname = sys.argv[2]

	random = parse_vcf(Rname) #run the function to load random_snippet.vcf
	dbSNP = parse_vcf(dbname) #run the function to load dbSNP.vcf

	#print(dbSNP)
	#Create a dictionary of positions and IDs from the dbSNP file
	dbdic={} #create the dictionary
	posdb=[] #create a list for further calculation
	for i in range(len(dbSNP)): 
	    pos = dbSNP[i][1] #get the position data (in the second column) as pos
	    posdb.append(pos) #store all the position data in a list for further use
	    id = dbSNP[i][2] # get the ID data(in the third column ) as ID
	    dbdic[pos]=(id) # make the dirctionary in which the key is position and the related value is the ID(gene)

	incorrect=0 # define a variable to calculate records that do not have a corresponding ID in  dbSNP ID dictionary

	# Replaces the ID in each record from random_snippet.vcf with the correct label, if it exists, from dbSNP dictionary(dbdic)
	for i in range(len(random)): 
	    if random[i][1] in posdb: # judge if same record appears in two data by the positon
	        random[i][2] = dbdic[pos] #if the recod exists in both file, replaces the ID with the ID in dbSNP
        
	    else:
	        incorrect=incorrect+1 # record how many position doesn't exist in both file, 

	print(incorrect) #print the results

The number of random_snippet.vcf records that do not have a corresponding ID in your dbSNP ID dictionary is 100
