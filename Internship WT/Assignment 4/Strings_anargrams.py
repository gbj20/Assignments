# 5. Check if two strings are anagrams.

def anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)


word1 = input("Enter first string: ")
word2 = input("Enter second string: ")

if anagrams(word1, word2):
    print("The strings are anagrams.")
else:
    print("The strings are NOT anagrams.")
