'''
l=[1,23,5,10]
print(all(l))    

l=[1,2,0]

print(all(l))     



s=[1,'',0]
print(any(s))    
s=[0,'']
print(any(s))

'''




print(list(filter(lambda n:(all(n%i!=0 for i in range(2,n//2+1))),[2,3,5,6,7,54,68,97,93,54,37,188,9,11,13,17,19,23,27,34])))



