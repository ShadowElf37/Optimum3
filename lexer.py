def tokenize(line):
    tokens = []
    buffer = ""
    for char in line:

        if char in ('=', '!', '~', '+', '-', '/', '*', '&', '$', '@', '*'):
            tokens.append(buffer)
            tokens.append('=')
            buffer = ""
            continue

        buffer += char
