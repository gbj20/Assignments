# 5. Check if a number is prime

num = int(input("Enter a Number :"))

if (num < 2):
    print(num, "Not Prime!!")
elif (num % 2 == 0 or num % 3 == 0 and num > 3):
    print(num, "is Not Prime!!")
else:
    print("prime")
