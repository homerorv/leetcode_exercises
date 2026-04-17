'''
https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/706/stacks-and-queues/4703/

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
 
Example 1:

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

'''
from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        self.total += val
        self.queue.append(val)
        while len(self.queue) > self.size:
            item = self.queue.popleft()
            self.total -= item
        res = self.total/len(self.queue)
        return res

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
'''
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
'''
sol = MovingAverage(3)
res = sol.next(1)
print(res)
res = sol.next(10)
print(res)
res = sol.next(3)
print(res)
res = sol.next(5)
print(res)
