text = "apple banana apple orange banana apple"
words = text.split()
count = {}
for word in words:
    count[word] = count.get(word,0) + 1
print(count)
for word, value in count.items():
    print(word,"appears",value,"times")