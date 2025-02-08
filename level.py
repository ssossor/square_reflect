import pygame
import tiles

class Level:
    def __init__(self, number: int, name: str, width: int, height: int, data: list) -> None:
        self.number = number
        self.name = name
        self.width = width
        self.height = height
        self.data = data
        self.tileslist = []
    
    def build(self) -> None:
        self.tileslist = []
        portal_memory = {}
        for i in range(len(self.data)):
            if self.data[i] == "00":
                self.tileslist.append(tiles.Empty())
            if self.data[i] == "01":
                self.tileslist.append(tiles.Block())
            if self.data[i] == "02":
                self.tileslist.append(tiles.GhostBlock())
            if self.data[i] == "03":
                self.tileslist.append(tiles.Key())
            if self.data[i] == "04":
                self.tileslist.append(tiles.Lock())
            if self.data[i] == "05":
                self.tileslist.append(tiles.Kill())
            if self.data[i] == "06":
                self.tileslist.append(tiles.Canon())
            if self.data[i][0] == "?":
                self.tileslist.append(tiles.Start(int(self.data[i][1])))
            if self.data[i][0] == "!":
                self.tileslist.append(tiles.End(int(self.data[i][1])))
            if self.data[i][0] == "A":
                self.tileslist.append(tiles.Angle(int(self.data[i][1])))
            if self.data[i][0] == "a":
                self.tileslist.append(tiles.GhostAngle(int(self.data[i][1])))
            if self.data[i][0] == "p":
                if self.data[i][1] in portal_memory:
                    self.tileslist[portal_memory[self.data[i][1]]] = tiles.Portal(self.data[i][1], i)
                    self.tileslist.append(tiles.Portal(self.data[i][1], portal_memory[self.data[i][1]]))
                else:
                    portal_memory[self.data[i][1]] = i
                    self.tileslist.append(tiles.Portal(self.data[i][1], '?'))

    def get_start_state(self) -> tuple[int, int]:
        for i in range(len(self.data)):
            if self.data[i][0] == "?":
                return i, int(self.data[i][1]), 0
    
    def draw(self, state: tuple[int, int], playertexture: pygame.Surface, screen: pygame.Surface) -> None:
        screen.fill((112, 154, 209))

        playerposition = state[0]
        playerdirection = state[1]

        screenwidth = screen.get_size()[0]
        screenheight = screen.get_size()[1]

        marginx = screenwidth * 0.1
        marginy = screenheight * 0.1

        if screenwidth * 0.8 / self.width > screenheight * 0.8 / self.height:
            tilesize = screenheight * 0.8 / self.height
            marginx = marginx + (screenwidth * 0.8 - self.width * tilesize) / 2
        else:
            tilesize = screenwidth * 0.8 / self.width
            marginy = marginy + (screenheight * 0.8 - self.height * tilesize) / 2

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(marginx - screenwidth / 256, marginy - screenwidth / 256, screenwidth - marginx * 2 + screenwidth / 128, screenheight - marginy * 2 + screenwidth / 128))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(marginx, marginy, screenwidth - marginx * 2, screenheight - marginy * 2))

        for i in range(len(self.tileslist)):
            if i == playerposition:
                screen.blit(pygame.transform.scale(playertexture, (tilesize, tilesize)), ((i % self.width) * tilesize + marginx, i // (self.width) * tilesize + marginy))
            else:
                screen.blit(pygame.transform.scale(self.tileslist[i].texture(), (tilesize, tilesize)), ((i % self.width) * tilesize + marginx, i // (self.width) * tilesize + marginy))
    
    def get_tiles_list(self) -> list:
        return self.tileslist
    
    def get_board_size(self) -> tuple[int, int]:
        return self.width, self.height
