def analyzetext(text):
    data = {"characters":len(text),"words":len(text.split()),"uppercase":0}
    for char in text:
        if char.isupper():
            data["uppercase"] += 1
    return data
print(analyzetext("Hello Python"))