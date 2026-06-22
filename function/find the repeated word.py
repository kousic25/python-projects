def mostcommonword(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word,0)+1
    result = max(
        frequency,
        key=frequency.get)
    return result
sentence = "apple banana apple orange apple banana"
print(mostcommonword(sentence))