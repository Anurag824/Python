def sum_of_current_and_previous(n):
    print(f"Printing current and previous number sum in a range({n})")
    for x in range(n):
        print(f"Current Number {x} Previous Number {x-1} Sum: {x+(x-1)}" if x>0 else f"Current Number {x} Previous Number {x} Sum: {x+x}")
    #for x in range(1,n):print(f"Current Number {x} Previous Number {x-1} Sum: {x+(x-1)}")
#PYnative exercise 2
#Print the sum of the current number and the previous number
n=int(input("Enter the max number:"))
sum_of_current_and_previous(n)