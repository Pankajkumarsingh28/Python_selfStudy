# Program to Reverse the string
str1=input("Enter the String: ")
str2=" "
n=len(str1)
print(n)
for i in range(n-1,-1,-1):
    str2=str2+str1[i]
print(str2)