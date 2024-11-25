l=eval(input())   # taking list as user input by using eval function
m=l[0]            # assuming that first element is the maximum element and assigning maximum element m as l[0] m=l[0]
for i in l:       # iterasting list l by using for loop
    if i>m:       # checking whether the extracted ele is greater than first value
        m=i       # if the extracted ele is greater update maximum ele as extracted ele so m=i
print(m)          # after completing the for loop print maximum element

''' input=[2,3,534,45,67]

maximum m=l[0]=2

iteration 1: it will extract 2 check whether 2 is greater than 2 or not false so still m=l[0]=2
iteration 2: it will extract 3 check whether 3 is greater than 2 or not true  so update m from 2 to 3 so m=3
iteration 3: it will extract 534 check whether 534 is greater than 3 or not true  so update m from 3 to 534 so m=534
iteration 4: it will extract 45 check whether 45 is greater than 534 or not false  so m=534
iteration 5: it will extract 67 check whether 67 is greater than 534 or not false  so m=534

at last print maximum m as 534'''
