import re
from .sequences import seqs


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f'<Token: {self.type} = {self.value!r}>'


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __repr__(self):
        return f'<Stack: {self.items}>'


def tokenize(string):
    tokens = []
    while len(string) > 0:
        # Match opening tags
        match = re.match(r'\[([a-zA-Z]*)\]', string)
        if match:
            tokens.append(Token('tag', match.group(1)))
            string = string[match.end():]
        else:
            # Match closing tags
            match = re.match(r'\[\/[a-zA-Z]*\]', string)
            if match:
                tokens.append(Token('close', ''))
                string = string[match.end():]
            else:
                tokens.append(Token('string', string[0]))
                string = string[1:]
    return tokens


def escape(token):
    if token.type == 'tag':
        if token.value in seqs:
            return f'\033[{seqs[token.value]}m'
        else:
            return ''


def tint(string):
    tokens = tokenize(string)
    stack = Stack()
    ret = ''
    for token in tokens:
        if token.type == 'tag':
            seq = escape(token)
            ret += seq
            stack.push(seq)
        elif token.type == 'close':
            stack.pop()
            ret += '\033[0m'
            for item in stack.items:
                ret += item
        elif token.type == 'string':
            ret += token.value
    return ret