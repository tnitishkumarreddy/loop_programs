s=input()
summ=0
for i in range(1,len(s),2):
    if s[i].isdigit() and int(s[i])%2==0:
        summ+=int(s[i])
print(summ)

''' s='hai1243556'
iteration 1: it will extract 1 and check s[1]='h' is digit or not false so still summ=0
iteration 2: it will extract 3 and check s[3]='1' is digit or not true and check int('1') is even or not false so still summ=0
iteration 3: it will extract 5 and check s[5]='4' is digit or not true and check int('4') is even or not true so add it to summ=0+4=4
iteration 4: it will extract 7 and check s[7]='5' is digit or not true and check int('5') is even or not false so still summ=4
iteration 5: it will extract 9 and check s[9]='6' is digit or not true and check int('6') is even or not true so add it to summ=4+6=10

at last print summ

'''
