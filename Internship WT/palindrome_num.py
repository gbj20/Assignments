# n = 121
# n = str(n)

# reverse = n[::-1]

# if (n == reverse):
#     print("palindrome")
# else:
#     print("Not Palindrome")
################################################
n = 121
a = n//100 #return 1
b = n % 100 # return 21
c = b//10 # return 2
d = b % 10 # return 1

if (a == d):
    print("palindrome")
else:
    print("Not Palindrome")


