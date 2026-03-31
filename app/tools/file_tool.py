def save_post(content):
    with open("data/posts.txt", "a") as f:
        f.write(content + "\n\n")