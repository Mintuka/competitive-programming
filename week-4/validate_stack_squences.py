class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = deque()
        pushed = deque(pushed)
        popped = deque(popped)
        while pushed:
            stack.append(pushed.popleft())
            while popped and stack and popped[0] == stack[-1]:
                    stack.pop()
                    popped.popleft()
        
        #Run time O(n)
        #Space cm O(n)
        return False if len(stack) else True