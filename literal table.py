import sys


literal_dict={}
def update_literal(i,var,size,line_no,hexVal):
    dict1={" "+str(i):{'variable':var,'size':size,'line_number':line_no,'hexadecimalValue':hexVal}}
    literal_dict.update(dict1)

def stringToHex(word1,array1):
    for i in range(0,len(word1)):
        y=ord(word1[i])
        y=hex(y)
        y=y[2:]
        array1.append(y)

def hexConversion(word,array1):
    if len(word)>=1:
        word=word.split(",")
        for i in range(0,len(word)):
            hexval=hex(int(word[i]))
            hexval=hexval[2:]
            array1.append(hexval)

def get_literal(fp):
    flag = 0
    fp=open(fp1,"r")
    line=fp.readline()
    i=0
    while line.find("main:")<=-1:
        array1=[]
        if line in ['\n','\t\n']:
            print("")
        else:
            y=line.find("dd")
            if y>-1:
                word=line[y+3:].strip("\n")
                hexConversion(word,array1)
                if(len(array1)>1):
                    array1=','.join(array1)
                else:
                    array1=''.join(array1)
                size='4'
                update_literal(i,word,size,flag,array1)
                i+=1
            else:
                y=line.find("db")
                if y>-1:
                    word1=line.find('"')
                    word=line[word1+1:].strip("\n")
                    word1=line.find('"')
                    word=line[:word1]
                    stringToHex(word,array1)
                    array1=''.join(array1)
                    size=1
                    update_literal(i,word,size,flag,array1)
                    i+=1
                elif(line.find("resb")>-1 or line.find("resd")>-1 or line.find("resq")>-1 ):
                    rb=line.find("resb")
                    if rb>-1:
                        reg=rb
                        size='1'
                    rd=line.find("resd")
                    if rd>-1:
                        word=rd
                        size='4'
                    rq=line.find("resq")
                    if rq>-1:
                        word=rq
                        size='8'
                    word=line[word+5:].strip("\n")
                    hexConversion(word,array1)
                    if(len(array1)>1):
                        array1=','.join(array1)
                    else:
                        array1=''.join(array1)
                    update_literal(i,word,size,flag,array1)
                    i+=1
        line=fp.readline()
        flag+=1

    while line:
        if line in ['\n','\t\n']:
           print("")
        else:
            line=line.split(' ')
            if len(line)>1:
                #print(line)
                line=line[1].split(',')
                #print(line)
                if len(line)>=1:
                    #print(line)
                    line=line[0].split()
                    #print(line)
                    line1=list(line[0])
                    kk=ord(line1[0])
                    if kk>=48 and kk<=57:
                        hexConversion(line[0],array1)
                        if(len(array1)>1):
                            array1=','.join(array1)
                        else:
                            array1=''.join(array1)
                        update_literal(i,line[0],'-',flag,array1)
                        i+=1
                        array1=[]
        line=fp.readline()
        flag+=1

def displayTable(literal_dict):
    print("\t\t\t\t\t\t\t--------LITERAL TABLE--------")
    print("Literal\t\t\tvarialble\t\t\tsize\t\t\tline_number\t\t\thexadecimalValue")
    print("___________________________________________________________________________________________________________________________________")
    for i in range(0,len(literal_dict)):
        print("%s\t\t\t%s\t\t\t%s\t\t\t%d\t\t\t%s"%(" "+str(i),literal_dict[" "+str(i)]['variable'],literal_dict[" "+str(i)]['size'],literal_dict[" "+str(i)]['line_number'],literal_dict[" "+str(i)]['hexadecimalValue']))

if __name__=="__main__":
    fp1=sys.argv[1]
    if fp1:
        print("File opened")
    else:
        print("File not found")
    get_literal(fp1)
    #displayTable(literal_dict)