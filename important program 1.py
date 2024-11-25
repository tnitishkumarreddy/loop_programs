s=input()
c=0
new=''
for i in s:
    if i=="1":
        c+=1
    else:
        new+=chr(64+c)
        c=0
print(new)




'''

input:  11101011110
output:  cad
        
'''
