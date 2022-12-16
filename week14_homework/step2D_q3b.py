bin_f=open('assembly.fasta','r')
lines=bin_f.readlines()

node=[]
for i in lines:
    if i.startswith(">"):
        node.append(i.split('_'))
#print(node)

length=[]
for i in node:
    i[3]=int(i[3])
    length.append(i[3])

print(sum(length))