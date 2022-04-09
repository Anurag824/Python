def taxable_income(income):
    n=income
    tax=0
    if n<=10000:
        tax=0
    elif n<=20000:
        n=n-10000
        tax=n*0.1
    else:
        tax=0
        tax=10000*0.1
        tax+=(n-20000)*0.2
    print(f"Tax on the current income: {income} is: {tax}")
#PYnative exercise 12
#Calculate income tax for the given income by adhering to the below rules
'''
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20'''
income=int(input("Enter income: "))
taxable_income(income)