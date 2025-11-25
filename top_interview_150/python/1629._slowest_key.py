'''
1629. Slowest Key
https://leetcode.com/problems/slowest-key/description/

A newly designed keypad was tested, where a tester pressed a sequence of n keys, one at a time.
You are given a string keysPressed of length n, where keysPressed[i] was the ith key pressed 
in the testing sequence, and a sorted list releaseTimes, where releaseTimes[i] was the time the ith key
 was released. Both arrays are 0-indexed. The 0th key was pressed at the time 0, and every subsequent 
 key was pressed at the exact time the previous key was released.
The tester wants to know the key of the keypress that had the longest duration. The ith keypress had a 
duration of releaseTimes[i] - releaseTimes[i - 1], and the 0th keypress had a duration of releaseTimes[0].

Note that the same key could have been pressed multiple times during the test, and these multiple presses 
of the same key may not have had the same duration.

Return the key of the keypress that had the longest duration. If there are multiple such keypresses, 
return the lexicographically largest key of the keypresses.

Example:

Input: releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
Output: "a"
Explanation: The keypresses were as follows:
Keypress for 's' had a duration of 12.
Keypress for 'p' had a duration of 23 - 12 = 11.
Keypress for 'u' had a duration of 36 - 23 = 13.
Keypress for 'd' had a duration of 46 - 36 = 10.
Keypress for 'a' had a duration of 62 - 46 = 16.
The longest of these was the keypress for 'a' with duration 16.
'''

from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        current_time = releaseTimes[0]
        idx = 0
        for i in range(1,len(releaseTimes)):
            new_time = release_times[i]-release_times[i-1]
            if new_time == current_time:
                if keysPressed[i] > keysPressed[idx]:
                    idx = i
                    current_time = new_time
            elif new_time > current_time:
                idx = i
                current_time = new_time                    

        return keysPressed[idx]
    

#release_times =  [12,23,36,46,62]
release_times =  [12,24,26,46,48]
key_pressed = "spuda"

sol = Solution()
answer = sol.slowestKey(release_times,key_pressed)
print(answer)




