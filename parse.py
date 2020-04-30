class Scanner:
    def __init__(self, len):
        self.l = len
        self.s = ""
    def push(self, c):
        if len(self.s) < self.l:
            self.s += c
        else:
            self.s = self.s[1:] + c

    def __eq__(self, other):
        return other == self.s

class Stateful:
    def __init__(self, enter, exit):
        self.enter = enter
        self.exit = exit

    def parse(self, text):
        blocks = []

        buffer1 = Scanner(len(self.enter))
        buffer2 = Scanner(len(self.exit))

        depth = 0
        general_buffer = ""

        for char in text:
            buffer1.push(char)
            buffer2.push(char)

            if buffer1 == self.enter:
                depth += 1
                if depth == 1:
                    blocks.append(general_buffer)
                    general_buffer = ""

            elif buffer2 == self.exit:
                depth -= 1
                if depth == 0:
                    blocks.append(general_buffer)
                    general_buffer = ""

            general_buffer += char

        blocks.append(general_buffer)
        return blocks




