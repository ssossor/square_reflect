import pygame

class Player:
    def __init__(self, startstate: tuple[int, int, int]) -> None:
        self.position = startstate[0]
        self.direction = startstate[1]
        self.numberkeys = startstate[2]
        self.texturepath = "C:\\squarereflect\\assets\\player.png"
        self.picture = pygame.image.load(self.texturepath).convert_alpha()
    
    def move(self, board: list, boardsize: tuple[int, int]):
        width = boardsize[0]
        height = boardsize[1]

        if self.direction == 1 and self.position < width:
            self.direction = 0

        elif self.direction == 2 and self.position % width == width - 1:
            self.direction = 0
        
        elif self.direction == 3 and self.position >= width * (height - 1):
            self.direction = 0
        
        elif self.direction == 4 and self.position % width == 0:
            self.direction = 0

        else:
            self.position, self.direction, self.numberkeys = board[self.get_next_pos(boardsize)].apply(self.get_state(), self.get_next_pos(boardsize))

    def get_next_pos(self, boardsize: tuple[int, int]) -> int:
        width = boardsize[0]
        height = boardsize[1]

        if self.direction == 1:
            return self.position - width
        
        if self.direction == 2:
            return self.position + 1
        
        if self.direction == 3:
            return self.position + width
        
        if self.direction == 4:
            return self.position - 1

    def get_state(self) -> tuple[int, int, int]:
        return (self.position, self.direction, self.numberkeys)
    
    def texture(self) -> pygame.Surface:
        return self.picture
    
    def move_up(self) -> None:
        self.direction = 1
    
    def move_right(self) -> None:
        self.direction = 2
    
    def move_down(self) -> None:
        self.direction = 3
    
    def move_left(self) -> None:
        self.direction = 4
    
    def finished(self) -> bool:
        return self.direction == 5
    
    def dead(self) -> bool:
        return self.direction == 6