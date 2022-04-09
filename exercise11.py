def reversed_num_by_string(n):
    for x in str(n)[::-1]:
        print(x,end=' ')
def reversed_num(n):
    while n>0:
        print(n%10,end=' ')
        n=n//10
#PYnative exercise 11
#Write a Program to extract each digit from an integer in the reverse order
n=int(input("Enter number to be reversed: "))
reversed_num(n)
#reversed_num_by_string(n)