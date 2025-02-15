'''
735. Asteroid Collision
We are given an array asteroids of integers representing asteroids in a row. 
The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). 
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
'''

'''
Gist:
Use a stack to maintain asteroids that haven't exploded.
If the current asteroid moves right (+), push it to the stack.
If the current asteroid moves left (-), check the stack.

Compare with the top asteroid (if it's moving right, +).
If the left-moving asteroid is smaller, it explodes.
If the right-moving asteroid is smaller, pop it.

Time: O(N)
Space: O(N)
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                break
        
            else:
                stack.append(asteroid)

        return stack
            