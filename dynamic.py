# Fibonacci Series

p = int(input("Enter length of Fibonacci Series\n>_"))
a = 0
b = 1
count = 2

if p<0:
    print("Enter only positive values")
elif p == 0:
    print(a)
elif p == 1:
    print(b)
else:
    print(a)
    print(b)
    while count<p:
        c=a+b
        print(c)
        count += 1
        a=b
        b=c
    
# # Removal of vowel from a given string
# str = input("Enter string\n>_")
# vowels_in_string = "aeiouAEIOU"

# print("Input String is " + str)
# for char in str:
#     if char in vowels_in_string:
#         str = str.replace (char, "")
# print ("Your new string is "+ str)