# Program to Reverse the string
# Program to Reverse the string
# This is comments for git demo
str1=input("Enter the string: ")
str2=""
n=len(str1)
print(n)
for i in range(n-1,-1,-1):
    str2=str2+str1[i]
print(str2)


if (str1==str2):

    print("The string is Palindrome")
else:
    print("The string is not Palindrome")
