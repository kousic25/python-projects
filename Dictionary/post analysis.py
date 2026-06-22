posts = {
    "post1": {"likes":500,"comments":50,"shares":20},
    "post2": {"likes":800,"comments":100,"shares":60}}
for post, data in posts.items():
    engagement = ( data["likes"] + data["comments"]*2 + data["shares"]*3)
    print(post,engagement)