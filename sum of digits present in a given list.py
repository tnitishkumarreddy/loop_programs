l=eval(input())
s=0
for i in l:
    if type(i)==int:
        s+=i
print(S)


''' input=[1,3,[23,45],'hai',5]

iteration 1: it will fetch 1 check datatype of 1 is int or not true so add i to s now s=0+1=1
iteration 2: it will fetch 3 check datatype of 3 is int or not true so add i to s now s=1+3=4
iteration 3: it will fetch [23,45] check datatype of [23,45] is int or not false so s=4 
iteration 4: it will fetch 'hai' check datatype of 'hai' is int or not false so s=4
iteration 5: it will fetch 5 check datatype of 5 is int or not true so add i to s now s=4+5=9


at last print s which is 9
'''

