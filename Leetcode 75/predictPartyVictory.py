'''
649. Dota2 Senate
In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".
'''

'''
Gist:
Store initial indices of R and D in separate queues.

Simulate rounds:
The senator with the earlier index gets to ban first.
The banned senator is removed.
The banning senator moves to the next round by adding n to its index. 

Continue until one queue is empty. Return the winning party based on which queue is not empty.

Time: O(N)
Space: O(N)
'''
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_queue = deque()
        dire_queue = deque()
        n = len(senate)

        # Store senator indices in queues
        for i, s in enumerate(senate):
            if s == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)

        # Process rounds until one queue is empty
        while radiant_queue and dire_queue:
            r_index = radiant_queue.popleft()
            d_index = dire_queue.popleft()

            # The senator with the smaller index bans the opponent
            if r_index < d_index:
                radiant_queue.append(r_index + n)  # Push back to queue for next round
            else:
                dire_queue.append(d_index + n)

        return "Radiant" if radiant_queue else "Dire"