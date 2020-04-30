import parse
import objects
import lexer

class Compiler:
    def __init__(self, text):
        self.text = text.replace('\t', '').replace('\n', '').replace(' ', '').replace('\r', '')
        self.code_objects = []
        self.compiled_code_objects = []

        self.text = self.construct_blocks()

    def construct_blocks(self, text=None):
        if text is None:
            text = self.text

        blocker = parse.Stateful('{', '}')
        raw_blocks = blocker.parse(text)
        rendered_blocks = []
        for block in raw_blocks:
            if block[0] == '{' and block[-1] == '}':
                co = objects.CodeObject(block.lstrip('{').rstrip('}'), self)
                self.code_objects.append(co)
                rendered_blocks.append(co.name)
                continue
            rendered_blocks.append(block)
        return ''.join(rendered_blocks)

    def compile_code_objects(self):
        for co in self.code_objects:
            self.compiled_code_objects.append((co.name, self.compile(co.code)))

    def compile(self, code=None):
        if code is None:
            code = self.text

        compiled = ''

        lines = code.split(';')
        for line in lines:
            tokens = lexer.tokenize(line)

            # LAYOUT
            #
            # state = None
            # states = {'if': Syntax(KW, EXPRESSION, CO), 'and': Syntax(NAME, KW, NAME), 'let': Syntax(NAME, KW, NAME)}
            # cache = []
            # if state is None:
            #   state = states.get(token)
            # cache.append(token)
            #
            # >> state.render(cache)



            for i, token in enumerate(tokens):
                ...



        return compiled


    def compile_all(self):
        codefs = '\n'.join(f"def {co.name}:\n\t{co.code}" for co in self.compiled_code_objects)
        comp = self.compile(self.text)
        return codefs + '\n\n# BEGIN\n\n' + comp