def divisible_by_five(l1,n):
    print(f"Divisible by {n}")
    for x in l1:
        if x%n==0:print(x)
#PYnative exercise 6
#Display numbers divisible by n from a list
l1=list(map(int,input("Enter the list: ").split()))
n=int(input("Enter divisor: "))
print(f"Given list is {l1}")
divisible_by_five(l1,n)