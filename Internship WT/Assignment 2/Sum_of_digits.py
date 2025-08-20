# Find sum of digits (245 → 11)

num = "245"
sum = 0
for digit in str(num):
    sum += int(digit)
print(sum)
