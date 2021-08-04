def write_file(filename="default.txt", content=None):
    with open(filename, 'w') as f:
        f.write(content)
    return


def read_file(filename="default.txt"):
    with open(filename, 'r') as f:
        content = f.read()
    return content
