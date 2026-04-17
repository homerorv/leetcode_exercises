'''
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
'''
from collections import deque
class MyStack:

    def __init__(self):
        self.main_queue = deque()
        self.aux_queue = deque()
        self.topp = None
        

    def push(self, x: int) -> None:
        self.main_queue.append(x)
        self.topp = x

    def pop(self) -> int:
        if not self.main_queue:
            return None

        while self.main_queue:
            num =  self.main_queue.popleft()
            if len(self.main_queue) == 0:
                res = num
            else:
                self.aux_queue.append(num)

        while self.aux_queue:
            num =  self.aux_queue.popleft()
            self.main_queue.append(num)
            
        if not self.main_queue:
             self.topp = None
        else:
            self.topp = self.main_queue[-1]
        return res
    
    def top(self) -> int:
        return self.topp

    def empty(self) -> bool:
        if len(self.main_queue) == 0:
            return True
        else:
            return False
            

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
top = obj.top()
print(top)
pop = obj.pop()
print(pop)
pop = obj.pop()
print(pop)
pop = obj.pop()
print(pop)
pop = obj.pop()
print(pop)