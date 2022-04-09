def new_list(l1,l2):
    print("Generating new list taking odd numbers from list 1 and even numbers from list 2: ")
    l3=[]
    for x in l1:
        if x%2!=0:
            l3.append(x)
    for x in l2:
        if x%2==0:
            l3.append(x)
    print(f"result list {l3}")
#PYnative exercise 10
#Create a new list from a two list using the following condition
l1=list(map(int,input("Enter List 1: ").split()))
l2=list(map(int,input("Enter List 2: ").split()))
new_list(l1,l2)