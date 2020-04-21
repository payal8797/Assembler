import sys
symbol_dict={}
def update_symbol(i,sym,ty,defi,size,add,line_no,occ):
    dict1={" "+str(i):{'symbol':sym,'type':ty,'defined/undefined':defi,'size':size,'address':add,'line_number':line_no,'occurence':occ}}
    symbol_dict.update(dict1)

def getSymbols(fp):
    fp=open(fp1,"r")
    line=fp.readline()
    i=0
    occ=0
    line_no=0
    cnt=0
    array=[]
    initial_add=0
    while line.find("main")<=-1:
        line_no=line_no+1
        if line.find("jle")>-1 or line.find(" dd") > -1 or line.find(" dw") > -1 or line.find("db") > -1 or line.find("resd") > -1: 
            
            if line.find(" dd") > -1:
                var=line.find(" dd")
                sym=line[0:var].strip("\t")
                ty='Variable'
                a=line.split(",")
                size=4*(len(a))
                array.append(sym)
                defi='Defined\t'
                if initial_add==0:
                    add1=0
                    initial_add=1
                else:
                    add1=add1+(size*len(sym))
                add2=int(add1)
                add=hex(add2)
                update_symbol(i,sym,ty,defi,size,add,line_no,occ)
                i=i+1
            elif line.find(" dw ") > -1:
                var=line.find(" dw ")
                sym=line[0:var].strip("\t")
                ty='Variable'
                a=line.split(",")
                size=2*(len(a))
                array.append(sym)
                defi='Defined\t'
                if initial_add==0:
                    add1=0
                    initial_add=1
                else:
                    add1=add1+(size*len(sym))
                add2=int(add1)
                add=hex(add2)
                update_symbol(i,sym,ty,defi,size,add,line_no,occ)
                i=i+1
            elif line.find("db") > -1:
                var=line.find("db")
                sym=line[0:var-1].strip("\t")
                ty='Variable'
                a=line.split(",")
                size=1*(len(a))
                array.append(sym)
                defi='Defined\t'
                if initial_add==0:
                    add1=0
                    initial_add=1
                else:
                    add1=add1+(size*len(sym))
                add2=int(add1)
                add=hex(add2)
                update_symbol(i,sym,ty,defi,size,add,line_no,occ)
                i=i+1
            elif line.find("resd") > -1:
                var=line.find("resd")
                sym=line[0:var-1].strip("\t")
                ty='Variable'
                size=4
                array.append(sym)
                defi='Defined\t'
                start=line.find("resd")
                end=line.find("\n")
                p1=line[start+5:end]
                p2=int(p1)
                #print(p2)
                if initial_add==0:
                    add=0
                    initial_add=1
                else:
                    add1=size*p2
                add2=int(add1)
                add=hex(add2)
                update_symbol(i,sym,ty,defi,size,add,line_no,occ)
                i=i+1
        line=fp.readline()
    while line:
        line_no=line_no+1
       
        cnt=cnt+1
        if line.find(":") > -1:
                colon_pos=line.find(":")
                sym=line[0:colon_pos]
                ty='Label\t'
                size=0
                array.append(sym)
                defi='Undefined'
                initial_add=0
                add1=cnt
                add2=int(add1)
                add=hex(add2)
                update_symbol(i,sym,ty,defi,size,add,line_no,occ)
                i=i+1
        elif line.find("jle") > -1:
                lab=line.find("jle")
                start=line.find("jle")
                end=line.find('\n')
                sym=line[start+4:end]
                ty='Label\t'
                size=0
                array.append(sym)  
                add1=0
                add2=int(add1)
                add=hex(add2)
                update_symbol(i,sym,ty,defi,size,add,line_no,occ)            
                i=i+1
        
        line=fp.readline()

    print(array)
    print("\nSymbol Table\n")
    print("Index\t","Symbol\t","Type\t","Defined/Undefined\t","Size\t","Address\t","Line Number\t","Occurence")
    print("--------------------------------------------------------------------------------------------------")
    return

def inc_count(str1,symbol_dict):
    for i in range(len(symbol_dict)):
        if symbol_dict[" "+str(i)]['symbol']==str1:
            symbol_dict[" "+str(i)]['occurence']=symbol_dict[" "+str(i)]['occurence']+1
            return

def get_occurence_count(fp,array,symbol_dict):
    fp=open(fp1,"r")
    fp.seek(0)
    line=fp.readline()
    while line:
        ll=line.split(' ')
        for l in ll:
            str1=l.strip('\t').strip(',').strip('\n').strip(":")
            if str1 in array:
                inc_count(str1,symbol_dict)
        line=fp.readline()        
    
def displayTable(symbol_dict):
    for i in range(len(symbol_dict)):
        print("%s\t%s\t%s\t%s\t%d\t%s\t\t%d\t\t\t%d"%(" "+str(i),symbol_dict[" "+str(i)]['symbol'],symbol_dict[" "+str(i)]['type'],symbol_dict[" "+str(i)]['defined/undefined'],symbol_dict[" "+str(i)]['size'],symbol_dict[" "+str(i)]['address'],symbol_dict[" "+str(i)]['line_number'],symbol_dict[" "+str(i)]['occurence']))

if __name__=="__main__":
    fp1=sys.argv[1]
    if fp1:
        print("\nFile opened\n")
    else:
        print("Cannot open the file") 
    getSymbols(fp1)
    #print(symbol_dict)
    #fp1.seek(0)
    array=[]
    get_occurence_count(fp1,array,symbol_dict)
    #displayTable(symbol_dict)
    