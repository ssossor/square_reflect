import pygame
import level
import player

class Menu:
    def __init__(self, levels: list) -> None:
        self.levels = levels
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def init(self, screen: pygame.Surface) -> None:

        menu = True

        background = pygame.image.load("./assets/menu.png").convert_alpha()
        play = pygame.image.load("./assets/play.png").convert_alpha()

        while menu:

            pygame.display.flip()

            mousex, mousey = pygame.mouse.get_pos()

            width = screen.get_size()[0]
            height = screen.get_size()[1]


            if mousex < width * 5 / 8 and mousex > width * 3 / 8 and mousey < height * 7 / 8 and mousey > height * 5 / 8:
                pygame.draw.rect(screen, (51, 71, 97), pygame.Rect(width * 4 / 10 - width / 128, height * 7 / 10 - width / 128, width / 5 + width / 64, height / 5 + width / 64))
                pygame.draw.rect(screen, (112, 154, 209), pygame.Rect(width * 4 / 10, height * 7 / 10, width / 5, height / 5))
                screen.blit(pygame.transform.scale(play, (width / 5, height / 5)), (width * 4 / 10, height * 7 / 10))
            
            else:
                screen.blit(pygame.transform.scale(background, (width, height)), (0, 0))
                screen.blit(pygame.transform.scale(play, (width / 5, height / 5)), (width * 4 / 10, height * 7 / 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    menu = False

                if event.type == pygame.MOUSEBUTTONDOWN and mousex < width * 5 / 8 and mousex > width * 3 / 8 and mousey < height * 7 / 8 and mousey > height * 5 / 8:

                    level_selection = True

                    while level_selection:

                        pygame.display.flip()

                        mousex, mousey = pygame.mouse.get_pos()

                        width = screen.get_size()[0]
                        height = screen.get_size()[1]

                        iconsize = min(width / 6, 200)

                        between_tiles_x = min((width - iconsize * 4) / 5, 150)
                        between_tiles_y = min((height - iconsize * 4) / 5, 100)

                        marginx = (width - iconsize * 4 - between_tiles_x * 3) / 2
                        marginy = (height - iconsize * 3 - between_tiles_y * 2) / 2

                        level_boxes_list = []

                        screen.fill((112, 154, 209))

                        for i in range(len(self.levels)):
                            pygame.draw.rect(screen, (255, 163, 177), pygame.Rect(i % 4 * (iconsize + between_tiles_x) + marginx, i // 4 * (iconsize + between_tiles_y) + marginy, iconsize, iconsize))

                            level_boxes_list.append((i % 4 * (iconsize + between_tiles_x) + marginx,
                                                     i % 4 * (iconsize + between_tiles_x) + marginx + iconsize,
                                                     i // 4 * (iconsize + between_tiles_y) + marginy,
                                                     i // 4 * (iconsize + between_tiles_y) + marginy+ iconsize))

                            text_surface = self.font.render(str(self.levels[i].number), False, (51, 71, 97))
                            margin_text_x = (iconsize - text_surface.get_size()[0]) / 2
                            margin_text_y = (iconsize - text_surface.get_size()[1]) / 2
                            screen.blit(text_surface, (i % 4 * (iconsize + between_tiles_x) + marginx + margin_text_x, i // 4 * (iconsize + between_tiles_y) + marginy + margin_text_y))

                        for i in range(len(level_boxes_list)):
                            if mousex > level_boxes_list[i][0] and mousex < level_boxes_list[i][1] and \
                                mousey > level_boxes_list[i][2] and mousey < level_boxes_list[i][3]:
                                pygame.draw.rect(screen, (51, 71, 97), pygame.Rect(level_boxes_list[i][0], level_boxes_list[i][2], iconsize, iconsize))
                                pygame.draw.rect(screen, (255, 163, 177), pygame.Rect(level_boxes_list[i][0] + iconsize / 20, level_boxes_list[i][2] + iconsize / 20, iconsize * 18 / 20, iconsize * 18 / 20))
                                text_surface = self.font.render(str(self.levels[i].number), False, (51, 71, 97))
                                margin_text_x = (iconsize - text_surface.get_size()[0]) / 2
                                margin_text_y = (iconsize - text_surface.get_size()[1]) / 2
                                screen.blit(text_surface, (i % 4 * (iconsize + between_tiles_x) + marginx + margin_text_x, i // 4 * (iconsize + between_tiles_y) + marginy + margin_text_y))
                    
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                level_selection = False

                            if event.type == pygame.QUIT:
                                level_selection = False
                                menu = False

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                for i in range(len(level_boxes_list)):
                                    if mousex > level_boxes_list[i][0] and mousex < level_boxes_list[i][1] and \
                                        mousey > level_boxes_list[i][2] and mousey < level_boxes_list[i][3]:

                                        my_level = self.levels[i]
                                        my_level.build()

                                        my_player = player.Player(my_level.get_start_state())

                                        level_running = True

                                        while level_running:

                                            pygame.display.flip()
                                            my_level.draw(my_player.get_state(), my_player.texture(), screen)


                                            for event in pygame.event.get():
                                                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                                    level_running = False
                                                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                                                    screen.fill((255, 255, 255))
                                                    my_level.build()
                                                    my_player = player.Player(my_level.get_start_state())
                                                if my_player.get_state()[1] == 0 and event.type == pygame.KEYDOWN:
                                                    if event.key == pygame.K_UP:
                                                        my_player.move_up()
                                                    elif event.key == pygame.K_RIGHT:
                                                        my_player.move_right()
                                                    elif event.key == pygame.K_DOWN:
                                                        my_player.move_down()
                                                    elif event.key == pygame.K_LEFT:
                                                        my_player.move_left()
                                                if event.type == pygame.QUIT:
                                                    level_running = False
                                                    level_selection = False
                                                    menu = False
                                            if my_player.get_state()[1] != 0:
                                                my_player.move(my_level.get_tiles_list(), my_level.get_board_size())
                                                my_level.draw(my_player.get_state(), my_player.texture(), screen)
                                                pygame.display.flip()
                                                pygame.time.wait(40)
                                            if my_player.finished():
                                                level_running = False
                                            if my_player.dead():
                                                screen.fill((255, 255, 255))
                                                my_level.build()
                                                my_player = player.Player(my_level.get_start_state())
                                        break
