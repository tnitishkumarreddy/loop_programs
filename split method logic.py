s=input()
de=input()
l=[]
n=''
for i in s:
    if i!=de:
        n+=i
    else:
        l.append(n)
        n=''
l.append(n)
print(l)


''' s='hello bello'  n='' l=[]
 iteration 1: it will extract 'h' and check 'h'!='l' true so add it to n so n='h' ,l=[]
 iteration 2: it will extract 'e' and check 'e'!='l' true so add it to n so n='he' ,l=[]
 iteration 3: it will extract 'l' and check 'l'!='l' false so go to s and add n='he' to l s0 l=['he'] and make n=''
 iteration 4: it will extract 'l' and check 'l'!='l' false so go to s and add n='' to l s0 l=['he',''] and make n=''
 iteration 5: it will extract 'o' and check 'o'!='l' true so add it to n so n='o' ,l=['he','']
 iteration 6: it will extract ' ' and check ' '!='l' true so add it to n so n=' ' ,l=['he','']
 iteration 7: it will extract 'b' and check 'b'!='l' true so add it to n so n=' ob' ,l=['he','']
 iteration 8: it will extract 'e' and check 'e'!='l' true so add it to n so n='obe' ,l=['he','']
 iteration 9: it will extract 'l' and check 'l'!='l' false so go to s and add n=' obe' to l so l=['he','',' obe'] and make n=''
 iteration 10: it will extract 'l' and check 'l'!='l' false so go to s and add n='' to l so l=['he','',' obe',''] and make n=''
 iteration 11: it will extract 'o' and check 'o'!='l' true so add it to n so n='o' ,l=['he','',' obe','']

 after completing all iterations now n='o' and add that to l so l=['he','',' obe','','o']

 at last print l

 '''
