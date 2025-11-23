'''
given an array for each subarray of a specified length, find the smallest element in the subarray, among all these smallest elements, determine the largest one.

the subarray are formed by taking consecutives elements starting from each position in the array with each subarray having the specified length.
The last valid subarray ends exactly at the last element of the array

Example: 

n = 5, the number of elements
arr=[1,2,3,4,5]
k = 2

result = 4

For subarray size k= 2 the subarrays are [1,2], [2,3],[3,4] and [4,5] and the minima are [1,2,3,4] 
the final answer is 4, the maximun of these
'''

from collections import deque

def max_of_window_minima(arr, k):
    dq = deque()  # will store indices of useful elements
    window_mins = []

    for i, val in enumerate(arr):

        # Remove elements out of this window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Maintain deque in increasing order (front always smallest)
        while dq and arr[dq[-1]] > val:
            dq.pop()

        dq.append(i)

        # Window starts at i-k+1
        if i >= k - 1:
            window_mins.append(arr[dq[0]])

    return max(window_mins)

# Example usage:
if __name__ == "__main__":  
    arr = [1,2,3,4,5]
    k = 2
    result = max_of_window_minima(arr, k)
    print(f"The maximum of the minimums of all sliding windows of size {k} is: {result}")