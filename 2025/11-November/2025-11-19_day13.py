#count number of vowel


str1 = input("Enter string :")
vowel = "aeiouAEIOYU"
count = 0

for ch in str1:
    if ch in vowel:
        count += 1
print(f"The string {str1} has {count} vowels .")
