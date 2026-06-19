word = "He is a good boy"
count = 0
for ch in word:
    if ch in "aeiouAEIOU":
        count += 1
print("Vowels:", count)  