# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
    def __init__(self):
        self._push_stack = Stack()
        self._pop_stack = Stack()

    def push(self, x: int) -> None:
        self._push_stack.push(x)

    def pop(self) -> int:
        if self._pop_stack.empty():
            self._prepare_pop()
        return self._pop_stack.pop()

    def _prepare_pop(self):
        while not self._push_stack.empty():
            x = self._push_stack.pop()
            self._pop_stack.push(x)

    def peek(self) -> int:
        if self._pop_stack.empty():
            self._prepare_pop()
        return self._pop_stack.top()

    def empty(self) -> bool:
        return self._push_stack.empty() and self._pop_stack.empty()


class Stack():
    def __init__(self):
        self._stack = []

    def push(self, x: int) -> None:
        self._stack.append(x)

    def pop(self) -> int:
        return self._stack.pop()

    def empty(self) -> bool:
        return len(self._stack) == 0

    def top(self) -> int:
        return self._stack[-1]

