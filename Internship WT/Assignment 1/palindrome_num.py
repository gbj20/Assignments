# n = 121
# n = str(n)

# reverse = n[::-1]

# if (n == reverse):
#     print("palindrome")
# else:
#     print("Not Palindrome")


n = 121
a = n//100
b = n % 100
c = b//10
d = b % 10

if (a == d):
    print("palindrome")
else:
    print("Not Palindrome")
