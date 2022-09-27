file=open("data.dat",'r') 
lines=file.readlines() 
c=0 
for element in lines: 
    if not element.strip(): 
        continue 
    if(element.count("1")%2==0)or(element.count("0")%3==0): c+=1 
    print(c)
