def list_first_and_last_same(l1):
    print(f"Given list: {l1}")
    print("True" if l1[0]==l1[len(l1)-1] else "False")
#PYnative exercise 5
#Check if the first and last number of a list is the same
# list(map(int,l1)) to convert each string input to int
l1=list(map(int,input("Enter a list separared by spaces: ").split()))
list_first_and_last_same(l1)