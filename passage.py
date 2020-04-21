symbol_dict={}
def update_symbol(i,sym,occ):
    dict1={" "+str(i):{'symbol':sym,'occurence':occ}}
    symbol_dict.update(dict1)

def get_symbol(fp,array):
    update_symbol(1,'the',0)
    update_symbol(2,'The',0)
    update_symbol(3,'a',0)
    update_symbol(4,'A',0)
    return

def inc_count(str1,symbol_dict):
    for i in range(1,len(symbol_dict)+1):
        if symbol_dict[" "+str(i)]['symbol']==str1:
            # print(symbol_dict[" "+str(i)]['symbol'])
            symbol_dict[" "+str(i)]['occurence']=symbol_dict[" "+str(i)]['occurence']+1
            return

def get_occurence_count(fp,array,symbol_dict):
    line=fp.readline()
    while line:
        ll=line.split(' ')
        for l in ll:
            str1=l.strip('\t').strip(',').strip('\n').strip(":").strip(")").strip("(").strip(".")
            if str1 in array:
                # print (str+1)
                inc_count(str1,symbol_dict)
        line=fp.readline()     

if __name__=="__main__":
    fp=open("readme.txt","r")
    if fp:
        print("\nFile opened\n")
    else:
        print("Cannot open the file")   
    array=['a','A','the','The']
    print(array)
    print("\n")
    print("Index\t","Symbol\t","Occurence\t")
    print("--------------------------")
    get_symbol(fp,array)
    fp.seek(0)
    get_occurence_count(fp,array,symbol_dict)
    # print(symbol_dict)
    for i in range(1,len(symbol_dict)+1):
        print("%s\t%s\t%d"%(" "+str(i),symbol_dict[" "+str(i)]['symbol'],symbol_dict[" "+str(i)]['occurence']))