bin_ass=open('assembly.kraken','r')
bin_1=open('bin.1.fa','r')
bin_2=open('bin.2.fa','r')
bin_3=open('bin.3.fa','r')
bin_4=open('bin.4.fa','r')
bin_5=open('bin.5.fa','r')
bin_6=open('bin.6.fa','r')
bin_7=open('bin.7.fa','r')
bin_8=open('bin.8.fa','r')

ass_lines=bin_ass.readlines()
bin_1_lines = bin_1.readlines()


ass=[]
ass_dic={}

for i in ass_lines:
    ass.append(i.split('\t'))
for i in ass:
    i[0]=i[0].split('_')       

for i in ass:
    ass_dic[int(i[0][1])] = i[1]


# in this script, I use bin.f1 as example and I run 8 time with all the bin file
bin_f1=[]
bin_1_lines = bin_1.readlines()

for i in bin_1_lines:
    if i.startswith(">"):
        bin_f1.append(i.split('_'))

bin_tax=[]

for i in bin_f1:
    a=int(i[1])
    #print(int(a))
    tax=ass_dic[a]
    bin_tax.append(tax)

print(set(bin_tax))