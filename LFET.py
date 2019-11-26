print("LFN Filename Extract Tool - LFET")
print("This tool extracts filename from LFN made by Y311J")
print("Please Input 32 byte hex!!\n")
lfnhex=input("Input LFN HEX!\n>> ")
print("")
print("Result: ")
print("------------------------------------")
hxds=lfnhex.split(' ')
hxds[0]="nope"
hxds[11]="nope"
hxds[12]="nope"
hxds[13]="nope"
hxds[26]="nope"
hxds[27]="nope"
namelist=[]
imsi=[]
string=""
for i in hxds:
    if i=="nope":
        pass
    else:
        if len(imsi)==1:
            imsi.append(i)
            string=imsi[1]
            string+=imsi[0]
            chrhex="0x"+string
            string=chr(int(chrhex,16))
            namelist.append(string)
            imsi=[]
        elif len(imsi)==0:
            imsi.append(i)
        else:
            print("Error")
            exit(0)
name=""
for i in namelist:
    name+=i
print(name)