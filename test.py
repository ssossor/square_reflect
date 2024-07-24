import pygame
import tiles

pygame.init()

screen = pygame.display.set_mode((600, 480))

angle_1 = tiles.Angle(1)
angle_2 = tiles.Angle(2)
angle_3 = tiles.Angle(3)
angle_4 = tiles.Angle(4)

#1

assert angle_1.apply((7, 1), 4) == (4, 2)
assert angle_1.apply((3, 2), 4) == (3, 0)
assert angle_1.apply((1, 3), 4) == (1, 0)
assert angle_1.apply((5, 4), 4) == (4, 3)

#2

assert angle_2.apply((7, 1), 4) == (4, 4)
assert angle_2.apply((3, 2), 4) == (4, 3)
assert angle_2.apply((1, 3), 4) == (1, 0)
assert angle_2.apply((5, 4), 4) == (5, 0)

#3

assert angle_3.apply((7, 1), 4) == (7, 0)
assert angle_3.apply((3, 2), 4) == (4, 1)
assert angle_3.apply((1, 3), 4) == (4, 4)
assert angle_3.apply((5, 4), 4) == (5, 0)

#4

assert angle_4.apply((7, 1), 4) == (7, 0)
assert angle_4.apply((3, 2), 4) == (3, 0)
assert angle_4.apply((1, 3), 4) == (4, 2)
assert angle_4.apply((5, 4), 4) == (4, 1)

print("youpi")

#for i in range(3):
#    pass
#print(i)
#if any(i == 3 for i in range(5)):
#    print(i)


for i in range(5):
    if i == 3 or i == 4:
        print(i)
        break