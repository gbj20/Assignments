# str = "madam"
# reverse = str[::-1]
# if (str == reverse):
#     print("palindrome")
# else:
#     print("Not Palindrome")

#########################
# using for Loop

str = "madam"
reverse = str[::-1]

for char in str:  # reverse = char + reverse
    if str == reverse:
        print("palindrome")
    else:
        print("Not palindrome")
    break

