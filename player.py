import math

class Bullet:
    def __init__(self, x, y, angle) -> None:
        self.x = x
        self.y = y
        self.angle = angle

    def tick(self):
        self.x+=math.cos(self.angle)*4
        self.y+=math.sin(self.angle)*4

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.bullets = []
    def add_bullet(self, angle):
        self.bullets.append(Bullet(self.x, self.y, angle))