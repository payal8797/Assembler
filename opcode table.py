opcodes_dict={}
def update_opcodes(i,opc,source_reg,dest_reg,line_no):
    dict1={" "+str(i):{'opcode':opc,'source register':source_reg,'destination register':dest_reg,'line number':line_no}}
    opcodes_dict.update(dict1)

opcodes=['mov','add','sub','mul','div','jmp','cmp','printf']
registers=['eax','ecx','edx','ebx','esp','ebp','esi','edi']

def get_opcodes(array,array1,array2,fp):  
    i=0
    line_no=0
    line=fp.readline()
    while line:
        line_no=line_no+1
        end=line.find(" ")
        op=line[0:end].strip("\t")
        if op in opcodes:
            start1=line.find(" ")
            #print(start1)
            end1=line.find(",")
            #print(end1)
            source_reg=line[start1+1:end1].strip('\t')
            if source_reg in registers:
                #print("reg:",source_reg)
                array1.append(source_reg)
            
            start2=line.find(",")
            end2=line.find("\n")
            dest_reg=line[start2+1:end2].strip("\t")
            if dest_reg in registers:
                #print("dest:",dest_reg)
                array2.append(dest_reg)
            array.append(op)
            update_opcodes(i,op,source_reg,dest_reg,line_no)
            i=i+1
            
        start=line.find("call")
        end=line.find("\n")
        op=line[start+5:end]
        if op in opcodes:
            start1=line.find("  ")
            end1=line.find("\n")
            source_reg=line[start1+7:end1].strip("\t")
            if source_reg in registers:
                array1.append(source_reg)

                start2=line.find(",")
                end2=line.find("\n")
                dest_reg=line[start2:end2].strip("\t").strip(" ")
            if dest_reg in registers:
                array2.append(dest_reg)
            array.append(op) 
            update_opcodes(i,op,source_reg,dest_reg,line_no)  
            i=i+1   
        line=fp.readline()
    
    #print(array)
    #print("reg:",array1)
    print("\nOpcode table:\n")
    print("Index\t","Opcode\t","\tSource register\t","\tDestination register\t","\tLine number\t")
    print("------------------------------------------------------------------------------------------")


if __name__=="__main__":
    fp=open("SymbolCollection_nasm.asm","r")
    if fp:
        print("File opened")
    else:
        print("File not found")
    array=[]
    array1=[]
    array2=[]
    get_opcodes(array,array1,array2,fp)
    #print(opcodes_dict)
    for i in range(len(opcodes_dict)):
        print("%s\t%s\t\t%s\t\t\t%s\t\t\t\t%d"%(" "+str(i),opcodes_dict[" "+str(i)]['opcode'],opcodes_dict[" "+str(i)]['source register'],opcodes_dict[" "+str(i)]['destination register'],opcodes_dict[" "+str(i)]['line number']))