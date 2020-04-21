my_dict={}
def update_symbol(id,name,occ):
    dict1={id:{'name':name,'occurence':occ}}
    my_dict.update(dict1)

def get_count(fp):
    before_the=[]
    after_the=[]
    before_a=[]
    after_a=[]
    update_symbol(1,'the',0)
    update_symbol(2,'a',0)
    line=fp.readline()
    tflag=0
    aflag=0.append
    while line:
        word=line.split(' ')
        for tmp in word:
            if tflag==1:
                after_the.append(tmp)
                tflag=0
            if aflag==1:
                after_a.append(tmp)
                aflag=0
            tmp=tmp.strip('\n').strip('\t').strip(',').strip(')').strip('(').strip('.').strip(':')
          
            if tmp=="THE" or tmp=="The" or tmp=="the":
                tflag=1
                before_the.append(prev)
                my_dict[1]['occurence']=my_dict[1]['occurence']+1
            elif tmp=="a" or tmp=="A":
                aflag=1
                before_a.append(prev)
                my_dict[2]['occurence']=my_dict[2]['occurence']+1
            prev=tmp
        line=fp.readline()
    print("before the:",before_the,"\n")
    print("after the:",after_the,"\n")
    print("before a:",before_a,"\n")
    print("after a:",after_a,"\n")

if __name__=="__main__":
    fp=open("readme.txt","r")
    get_count(fp)
    print("Count of the : ",my_dict[1]['occurence'])
    print("Count of a : ",my_dict[2]['occurence'])