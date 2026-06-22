def comment_analysis(comments):
    result = {"positive":0,"negative":0}
    for comment in comments:
        if "good" in comment.lower():
            result["positive"] += 1
        if "bad" in comment.lower():
            result["negative"] += 1
    return result
comments = ["good video","bad explanation","good content"]
print(comment_analysis(comments))