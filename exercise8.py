def pattern(x):
    for a in range(1,x+1):
        for b in range(a):
            print(a,end='')
        print('')
'''PYnative exercise 8
Print the following pattern
1
22
333
4444
---
nnnnnn
'''
x=int(input("Enter n: "))
pattern(x)