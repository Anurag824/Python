def palindrome_via_string(n):
    print("Checking via String method")
    print("True" if str(n)==str(n)[::-1] else "False")
def palindrome(n):
    rev=0
    num=n
    while n>0:
        rev=(rev*10)+n%10
        n=n//10
    print("Checking via int method")
    print("True" if rev==num else "False")
#PYnative exercise 9
#Check Palindrome Number
n=int(input())
palindrome(n)
#palindrome_via_string(n)