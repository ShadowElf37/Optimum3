class CodeObject:
    COUNTER = 0

    def __init__(self, code, compiler):
        self.code = code
        self.compiler = compiler
        self.name = '__OptimumCodeObject_%d' % self.COUNTER
        self.COUNTER += 1

        self.code = self.compiler.construct_blocks(self.code)

class Context:
    def __init__(self, globals: dict, **vars):
        self.vars = vars
        self.globals = globals
        self.old_globals = {}

    def __enter__(self):
        for var in self.vars.keys():
            if val := self.globals.get(var):
                self.old_globals[var] = val
        self.globals.update(self.vars)
    def __exit__(self):
        for key in self.vars.keys():
            del self.globals[key]
        self.globals.update(self.old_globals)
        del self.globals, self.vars, self.old_globals
