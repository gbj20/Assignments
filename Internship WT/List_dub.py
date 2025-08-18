List = [1, 1, 2, 2, 3, 3, 4, 4, 5]
duplicates = []
for x in List:
    if x not in duplicates:
        duplicates.append(x)
print(duplicates)

# 2nd way : convert the list into set
a = [1, 2, 2, 63, 4, 4, 5]
a = list(set(a))
print(a)
