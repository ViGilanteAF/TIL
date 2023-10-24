from collections import deque


def solution(priorities, location):
    # [1,2,2,3]
    stack = sorted(priorities)
    waiting = deque(enumerate(priorities))
    order = 1
    while waiting:
        idx, process = waiting.popleft()
        if process != stack[-1]:
            waiting.append((idx, process))
        else:
            if idx == location:
                return order
            stack.pop()
            order += 1
