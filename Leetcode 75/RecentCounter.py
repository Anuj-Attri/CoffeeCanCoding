'''
933. Number of Recent Calls
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
'''
'''
Gist:
Use a queue (deque) to store timestamps of requests.
For each ping(t), remove all requests older than t - 3000 from the queue.
Return the number of elements remaining in the queue (valid requests).

Time: O(1)
Space: O(N)
'''
from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()  # Store request timestamps

    def ping(self, t: int) -> int:
        self.queue.append(t)  # Add new request

        # Remove outdated requests
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)  # Remaining requests within range

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)