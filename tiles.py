import pygame

class Empty:
    def __init__(self) -> None:
        self.texturepath = "./assets/empty.png"
        self.picture = pygame.image.load(self.texturepath).convert_alpha()
    
    def apply(self, state: tuple[int, int, int], nextpos: int) -> tuple[int, int, int]:
        position = state[0]
        direction = state[1]
        numberkeys = state[2]

        return (nextpos, direction, numberkeys)
    
    def texture(self) -> pygame.Surface:
        return self.picture
    
class Block:
    def __init__(self) -> None:
        self.texturepath = "./assets/block.png"
        self.picture = pygame.image.load(self.texturepath).convert_alpha()
    
    def apply(self, state: tuple[int, int, int], nextpos: int) -> tuple[int, int, int]:
        position = state[0]
        direction = state[1]
        numberkeys = state[2]

        return (position, 0, numberkeys)

    def texture(self) -> pygame.Surface:
        return self.picture
    
class Start:
    def __init__(self, direction: int) -> None:
        self.direction = direction
        if self.direction == 1:
            self.texturepath = "./assets/start_up.png"
        if self.direction == 2:
            self.texturepath = "./assets/start_right.png"
        if self.direction == 3:
            self.texturepath = "./assets/start_down.png"
        if self.direction == 4:
            self.texturepath = "./assets/start_left.png"
        self.picture = pygame.image.load(self.texturepath).convert_alpha()
    
    def apply(self, state: tuple[int, int, int], nextpos: int) -> tuple[int, int, int]:
        position = state[0]
        direction = state[1]
        numberkeys = state[2]

        newposition = position
        newdirection = 0

        if self.direction == 1 and direction == 3:
            newposition = nextpos
            newdirection = 1

        if self.direction == 2 and direction == 4:
            newposition = nextpos
            newdirection = 2
        
        if self.direction == 3 and direction == 1:
            newposition = nextpos
            newdirection = 3

        if self.direction == 4 and direction == 2:
            newposition = nextpos
            newdirection = 2

        return (newposition, newdirection, numberkeys)

    def texture(self) -> pygame.Surface:
        return self.picture

class End:
    def __init__(self, direction: int) -> None:
        self.direction = direction
        if self.direction == 1:
            self.texturepath = "./assets/end_up.png"
        if self.direction == 2:
            self.texturepath = "./assets/end_right.png"
        if self.direction == 3:
            self.texturepath = "./assets/end_down.png"
        if self.direction == 4:
            self.texturepath = "./assets/end_left.png"
        self.picture = pygame.image.load(self.texturepath).convert_alpha()
    
    def apply(self, state: tuple[int, int, int], nextpos: int) -> tuple[int, int, int]:
        position = state[0]
        direction = state[1]
        numberkeys = state[2]

        newposition = position
        newdirection = 0

        if direction == self.direction:
            newposition = nextpos
            newdirection = 5

        return (newposition, newdirection, numberkeys)

    def texture(self) -> pygame.Surface:
        return self.picture
    
class Angle:
    def __init__(self, direction) -> None:
        self.direction = direction
        if self.direction == 1:
            self.texturepath = "./assets/angle_top_left.png"
        if self.direction == 2:
            self.texturepath = "./assets/angle_top_right.png"
        if self.direction == 3:
            self.texturepath = "./assets/angle_bot_right.png"
        if self.direction == 4:
            self.texturepath = "./assets/angle_bot_left.png"
        self.picture = pygame.image.load(self.texturepath).convert_alpha()
    
    def apply(self, state: tuple[int, int, int], nextpos) -> tuple[int, int, int]:
        position = state[0]
        direction = state[1]
        numberkeys = state[2]

        newposition = position
        newdirection = 0

        if direction == self.direction or direction == (self.direction + 2) % 4 + 1:
            newposition = nextpos
            if self.direction == direction:
                newdirection = direction % 4 + 1
            else:
                newdirection = (self.direction + 1) % 4 + 1
        
        return newposition, newdirection, numberkeys
    
    def texture(self) -> pygame.Surface:
        return self.picture
    
class GhostBlock:
    def __init__(self) -> None:
        self.state = 0
        self.texturepath = "./assets/ghost_block.png"
        self.picture = pygame.image.load(self.texturepath).convert_alpha()
    
    def apply(self, state: tuple[int, int, int], nextpos: int) -> tuple[int, int, int]:
        position = state[0]
        direction = state[1]
        numberkeys = state[2]

        if self.state == 0:
            self.texturepath = "./assets/block.png"
            self.picture = pygame.image.load(self.texturepath).convert_alpha()
            self.state = 1
            return (nextpos, direction, numberkeys)

        return (position, 0, numberkeys)

    def texture(self) -> pygame.Surface:
        return self.picture

class GhostAngle:
    def __init__(self, direction) -> None:
        self.state = 0
        self.direction = direction
        if self.direction == 1:
            self.texturepath = "./assets/ghost_angle_top_left.png"
        if self.direction == 2:
            self.texturepath = "./assets/ghost_angle_top_right.png"
        if self.direction == 3:
            self.texturepath = "./assets/ghost_angle_bot_right.png"
        if self.direction == 4:
            self.texturepath = "./assets/ghost_angle_bot_left.png"
        self.picture = pygame.image.load(self.texturepath).convert_alpha()
    
    def apply(self, state: tuple[int, int, int], nextpos: int) -> tuple[int, int, int]:
        position = state[0]
        direction = state[1]
        numberkeys = state[2]

        if self.state == 0:
            if self.direction == 1:
                self.texturepath = "./assets/angle_top_left.png"
            if self.direction == 2:
                self.texturepath = "./assets/angle_top_right.png"
            if self.direction == 3:
                self.texturepath = "./assets/angle_bot_right.png"
            if self.direction == 4:
                self.texturepath = "./assets/angle_bot_left.png"
            self.picture = pygame.image.load(self.texturepath).convert_alpha()
            self.state = 1
            return (nextpos, direction, numberkeys)

        newposition = position
        newdirection = 0

        if direction == self.direction or direction == (self.direction + 2) % 4 + 1:
            newposition = nextpos
            if self.direction == direction:
                newdirection = direction % 4 + 1
            else:
                newdirection = (self.direction + 1) % 4 + 1
        
        return newposition, newdirection, numberkeys

    def texture(self) -> pygame.Surface:
        return self.picture
    
class Key:
    def __init__(self) -> None:
        self.state = 0
        self.texturepath = "./assets/key.png"
        self.picture = pygame.image.load(self.texturepath).convert_alpha()

    def apply(self, state: tuple[int, int, int], nextpos: int) -> tuple[int, int, int]:
        position = state[0]
        direction = state[1]
        numberkeys = state[2]

        if self.state == 0:
            self.state = 1
            self.texturepath = "./assets/empty.png"
            self.picture = pygame.image.load(self.texturepath).convert_alpha()
            return nextpos, direction, numberkeys + 1

        return nextpos, direction, numberkeys
    
    def texture(self) -> pygame.Surface:
        return self.picture
    
class Lock:
    def __init__(self) -> None:
        self.state = 0
        self.texturepath = "./assets/lock.png"
        self.picture = pygame.image.load(self.texturepath).convert_alpha()
    
    def apply(self, state: tuple[int, int, int], nextpos: int) -> tuple[int, int, int]:
        position = state[0]
        direction = state[1]
        numberkeys = state[2]

        if self.state == 0:
            if numberkeys > 0:
                self.state = 1
                self.texturepath = "./assets/empty.png"
                self.picture = pygame.image.load(self.texturepath).convert_alpha()
                return nextpos, direction, numberkeys - 1

            else:
                return position, 0, numberkeys

        return nextpos, direction, numberkeys
    
    def texture(self) -> pygame.Surface:
        return self.picture
    
class Kill:
    def __init__(self) -> None:
        self.texturepath = "./assets/kill.png"
        self.picture = pygame.image.load(self.texturepath).convert_alpha()

    def apply(self, state: tuple[int, int, int], nextpos: int) -> tuple[int, int, int]:
        position = state[0]
        direction = state[1]
        numberkeys = state[2]

        return nextpos, 6, numberkeys
    
    def texture(self) -> pygame.Surface:
        return self.picture
    
class Portal:
    def __init__(self, letter: str, otherpos) -> None:
        self.otherpos = otherpos
        self.texturepath = "./assets/portal" + letter + ".png"
        self.picture = pygame.image.load(self.texturepath).convert_alpha()
    
    def apply(self, state: tuple[int, int, int], nextpos: int) -> tuple[int, int, int]:
        position = state[0]
        direction = state[1]
        numberkeys = state[2]

        return self.otherpos, direction, numberkeys
    
    def texture(self) -> pygame.Surface:
        return self.picture

class Canon:
    def __init__(self) -> None:
        self.texturepath = "./assets/canon.png"
        self.picture = pygame.image.load(self.texturepath).convert_alpha()
    
    def apply(self, state: tuple[int, int, int], nextpos: int) -> tuple[int, int, int]:
        position = state[0]
        direction = state[1]
        numberkeys = state[2]

        return nextpos, 0, numberkeys
    
    def texture(self) -> pygame.Surface:
        return self.picture
