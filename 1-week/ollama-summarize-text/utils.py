

def store_file(path: str, text: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)