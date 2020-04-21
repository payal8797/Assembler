 
stud_dict={}
def update_sym(i,n,a):
    dict1={"id:"+str(i):{'name':n,'add':a}}   
    stud_dict.update(dict1)

if __name__=="__main__":
    n=int(input("Enter total elements:"))
    for i in range(n):
        st=input("Enter name:")
        a=input("Enter add:")
        update_sym(i,st,a)
    
    #print(sym_dict)
    i=0
    for i in range(len(stud_dict)):
        if stud_dict["id:"+str(i)]['name']=="payal":
            print(stud_dict["id:"+str(i)]['add'])
            break
