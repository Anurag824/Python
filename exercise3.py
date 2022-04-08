def even_index_chars(str):
    print("Printing only even index chars")
    #for x in range(len(str)):print(str[x]+"\n" if x%2==0 else '',end='')
    #for x in range(0,len(str),2):print(str[x])
    #via list
    for i in list(str)[0::2]:print(i)
#PYnative exercise 3
#Print characters from a string that are present at an even index number
str=input()
print(f"Original String is {str}")
even_index_chars(str)