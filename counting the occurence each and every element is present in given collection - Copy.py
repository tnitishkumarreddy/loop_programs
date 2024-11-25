cdt=eval(input())
d={}
for i in cdt:
    d[i]=cdt.count(i)
print(d)


#another method
cdt=eval(input())
d={}
for i in cdt:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)



''' input='harshad'

iteration 1: it will extract 'h' check if 'h' is not present in d true so create a key with 'h' and its value as 1 so d={'h':1}
iteration 2: it will extract 'a' check if 'a' is not present in d true so create a key with 'a' and its value as 1 so d={'h':1.'a':1}
iteration 3: it will extract 'r' check if 'r' is not present in d true so create a key with 'r'and its value as 1  so d={'h':1,'a':1,'r':1}
iteration 4: it will extract 's' check if 's' is not present in d true so create a key with 's' and its value as 1 so d={'h':1,'a':1,'r':1,'s':1}
iteration 5: it will extract 'h' check if 'h' is not present in d false so extract the value of 'h' key and add 1 to it so value of 'h' key becomes 2 so d={'h':2,'a':1,'r':1,'s':1}
iteration 6: it will extract 'a' check if 'a' is not present in d false so extract the value of 'a' key and add 1 to it so value of 'a' key becomes 2 so d={'h':2,'a':2,'r':1,'s':1}
iteration 7: it will extract 'd' check if 'd' is not present in d true so create a key with 'd'and its value as 1  so d={'h':2,'a':2,'r':1,'s':1,'d':1}

'''
