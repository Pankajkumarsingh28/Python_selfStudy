str1=' I am Pankaj Kumar     '
str2='I AM PANKAJ KUMAR'
print(str1)
print(str1.lstrip())
print(str1.rstrip())
str=str1.strip()
if str.lower()==str2.lower():
    print("String are same")
else:
    print("String are different")

# This is for Comparing two string and can be pushed to git