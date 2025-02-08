import twmap
import numpy

import tiles

map = twmap.Map("sr_test.map")

#help(map)

#help(map.groups)

#levels_layer = map.groups[2].__getattribute__("layers")

#for layer in levels_layer:
#    print(layer.name)
#    print(layer.tiles)

#help(levels_layer[0])

#print(len(map.groups[2].__getattribute__("layers")[0]))

#créer un deuxième groupe et ajouter un layer pour chaque niveau

def load_levels(path_to_file):
    map = twmap.Map(path_to_file)
    levels = map.groups[2].__getattribute__("layers")

    for level in levels:
        print(level.name)

        tmp_level = []

        width = len(level.tiles)
        height = len(level.tiles[0])

        for row in level.tiles:
            for tile in row:
                match tile[0]:
                    case 0: tmp_level.append("00")
                    case 1: tmp_level.append("01")
                    case 2: tmp_level.append("02")
                    case 3: tmp_level.append("03")
                    case 4: tmp_level.append("04")
                    case 5: tmp_level.append("05")
                    case 6: tmp_level.append("06")
                    case 7:
                        match tile[1]:
                            case 0: tmp_level.append("?1")
                            case 1: tmp_level.append("?1")
                            case 2: tmp_level.append("?3")
                            case 3: tmp_level.append("?3")
                            case 8: tmp_level.append("?2")
                            case 9: tmp_level.append("?2")
                            case 10: tmp_level.append("?4")
                            case 11: tmp_level.append("?4")
                    case 8:
                        match tile[1]:
                            case 0: tmp_level.append("!1")
                            case 1: tmp_level.append("!1")
                            case 2: tmp_level.append("!3")
                            case 3: tmp_level.append("!3")
                            case 8: tmp_level.append("!2")
                            case 9: tmp_level.append("!2")
                            case 10: tmp_level.append("!4")
                            case 11: tmp_level.append("!4")
                    case 9:
                        match tile[1]:
                            case 0: tmp_level.append("A2")
                            case 1: tmp_level.append("A1")
                            case 2: tmp_level.append("A3")
                            case 3: tmp_level.append("A4")
                            case 8: tmp_level.append("A3")
                            case 9: tmp_level.append("A2")
                            case 10: tmp_level.append("A4")
                            case 11: tmp_level.append("A1")
                    case 10:
                        match tile[1]:
                            case 0: tmp_level.append("a2")
                            case 1: tmp_level.append("a1")
                            case 2: tmp_level.append("a3")
                            case 3: tmp_level.append("a4")
                            case 8: tmp_level.append("a3")
                            case 9: tmp_level.append("a2")
                            case 10: tmp_level.append("a4")
                            case 11: tmp_level.append("a1")
                    case 11: tmp_level.append("pa")
                    case 12: tmp_level.append("pb")
                    case 13: tmp_level.append("pc")
                    case 14: tmp_level.append("pd")
                    case 15: tmp_level.append("pe")
        print(tmp_level)
        
load_levels("sr_test.map")