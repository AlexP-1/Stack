
class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def hooks(open, close):
    open_hooks = '[{('
    close_hooks = ']})'
    return open_hooks.index(open) == close_hooks.index(close)


def check_balance(list):
    stack = Stack()
    balance = True
    index = 0
    while index < len(list) and balance:
        sym = list[index]
        if sym in '[{(':
            stack.push(sym)
        else:
            if stack.isEmpty():
                balance = False
            else:
                top = stack.pop()
                if not hooks(top, sym):
                    balance = False
        index += 1
    if balance and stack.isEmpty():
        return True
    else:
        return False


if __name__ == "__main__":
    print(check_balance('(((([{}]))))'))
    print(check_balance('[([])((([[[]]])))]{()}'))
    print(check_balance('{{[()]}}'))
    print(check_balance('}{}'))
    print(check_balance('{{[(])]}}'))
    print(check_balance('[[{())}]'))