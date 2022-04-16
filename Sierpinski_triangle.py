import pygame
import random

pygame.init()

width = 300
height = 300
FPS = 30

window = pygame.display.set_mode((width, height), 0, 32)
window.fill((255, 255, 255))
clock = pygame.time.Clock()

# 3 points
print("Input 3 points! (within the range of (0, 300) for all values")
p1 = tuple(map(int, input("Point 1: >").split()))
p2 = tuple(map(int, input("Point 2: >").split()))
p3 = tuple(map(int, input("Point 3: >").split()))


loops = int(input("How many times to place points?: "))
mul = int(input("How many updates per call?: "))

"""Test input
0 300
300 300
150 0
25000
5
"""


class Sierpinski:
    """the script"""
    def __init__(self, window, loops, p1, p2, p3):
        """Constructor"""
        self.times = loops
        self.window = window
        self.points = [p1, p2, p3]
        self.color = (0, 0, 0)
        self.mul = 1

        # draw a random point within triangle
        self.first = [(p1[0] + p2[0] + p3[0]) // 3, (p1[1] + p2[1] + p3[1]) // 3]
        window.set_at(self.first, self.color)
    
    def calculate_midpoint(self, p1, p2):
        """get the midpoint"""
        return ((p1[0] + p2[0])//2, (p1[1] + p2[1]) // 2)
    
    def update(self):
        """update and calculate the next point"""
        for i in range(self.mul):
            base = random.choice(self.points)
            self.first = self.calculate_midpoint(base, self.first)
            self.window.set_at(self.first, self.color)



triangle = Sierpinski(window, loops, p1, p2, p3)
triangle.mul = mul

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    
    triangle.update()
    
    pygame.display.update()
    clock.tick(FPS)



