# a* path finding
# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

# build board
## square board with ring shape arena
## Spawns 1 & 2
## Walls 0

from typing import List
from hashlib import new

class board:
    def __init__(self, board: list):
        self.board = board
        self.accessible = self.accessible_terrain()
        self.pieces = {} # may be managed else where


    def accessible_terrain(self) -> list:
        accessible = []
        loc = ()
        for y, column in enumerate(self.board):
            for x, cell in enumerate(column):
                if not cell:
                    loc = (x,y)
                    accessible.append(loc)
        return accessible


    def add_piece(self, id: int, data: dict):
        # intake a unit or object
        pass

    def spawn_on_board(self):
        # for piece in pieces add to board
        pass

    def current_loc(self, id: int) -> tuple:
        for y, column in enumerate(self.board):
            for x, cell in enumerate(column):
                if id in cell:
                    return (x,y)


    def move(self, loc: tuple, direction: str, magnitued: int) -> tuple:

        x, y = loc
        new_loc = ()
        
        # n, s, e, w, ne, nw, se, sw
        if direction == "n":
            new_y = y - magnitued
            new_x = x
            new_loc = (new_x, new_y)
        elif direction == "s":
            new_y = y + magnitued
            new_x = x
            new_loc = (new_x, new_y)
        elif direction == "e":
            new_y = y
            new_x = x + magnitued
            new_loc = (new_x, new_y)
        elif direction == "w":
            new_y = y
            new_x = x - magnitued
            new_loc = (new_x, new_y)
        elif direction == "ne":
            new_y = y - magnitued
            new_x = x + magnitued
            new_loc = (new_x, new_y)
        elif direction == "nw":
            new_y = y - magnitued
            new_x = x - magnitued
            new_loc = (new_x, new_y)
        elif direction == "se":
            new_y = y + magnitued
            new_x = x + magnitued
            new_loc = (new_x, new_y)
        elif direction == "sw":
            new_y = y + magnitued
            new_x = x - magnitued
            new_loc = (new_x, new_y)
        else:
            print("unknown path")
            return loc
        return new_loc


    def valid_moves(self, loc: tuple, magnitue: int) -> list:
        valid_moves = []
        valid_move = ()
        directions = ["n", "s", "e", "w", "ne", "nw", "se", "sw"]
        for direction in directions:
            for i in range(magnitue+1):
                move_option = self.move(loc, direction, i)
                if move_option in self.accessible_terrain():
                    valid_move = (move_option, direction)
                    valid_moves.append(valid_move)
        return valid_moves


    def shortest_path(self, start: tuple, end: tuple) -> list:
        
        list_of_moves = []
        
        # TODO: use valid_moves
        # TODO: change to node based a*
        x1, y1 = start
        x2, y2 = end

        key = True
        while key:

                if x1 < x2:
                    x1 = x1 + 1 
                elif x1 > x2:
                    x1 = x1 - 1
                else:
                    x1 = x1

                if y1 < y2:
                    y1 = y1 + 1
                elif  y1 > y2:
                    y1 = y1 - 1
                else:
                    y1 = y1

                cord: tuple = (x1, y1)
                list_of_moves.append(cord)
                if end in list_of_moves:
                    key = False

        return list_of_moves


    def commit_move(self, current_loc: tuple, new_loc: tuple):
        x1, y1 = current_loc
        x2, y2 = new_loc

        # TODO: check for unit type if can move 
        
        # get id at current_loc
        current_loc_ids = self.ids_in_cells(current_loc)
        new_loc_ids = self.ids_in_cells(new_loc)
        # update new_loc with id
        self.board[y2][x2] = list(set().union(current_loc_ids, new_loc_ids))
        # remove id from current_loc
        self.board[y1][x1] = []


    def ids_in_cells(self, current_loc: tuple) -> list:
        x, y = current_loc
        ids : list = self.board[y][x]
        return ids



if __name__ == "__main__":

    map1 = [
        [[0],[0],[0],[0],[0], [], [], [],[0],[0],[0],[0],[0]],
        [[0],[0],[0], [], [], [], [], [], [], [],[0],[0],[0]],
        [[0],[0], [], [], [], [], [], [], [], [], [],[0],[0]],
        [[0], [], [], [], [], [], [], [], [], [1],[], [],[0]],
        [[0], [], [], [], [], [], [], [], [], [], [], [],[0]],
        [ [], [], [], [], [], [], [], [], [], [], [], [], []],
        [ [], [], [], [], [], [], [], [], [], [], [], [], []],
        [ [], [], [], [], [], [], [], [], [], [], [], [], []],
        [[0], [], [], [], [], [], [], [], [], [], [], [],[0]],
        [[0], [], [], [2],[], [], [], [], [], [], [], [],[0]],
        [[0],[0], [], [], [], [], [], [], [], [], [],[0],[0]],
        [[0],[0],[0], [], [], [], [], [], [], [],[0],[0],[0]],
        [[0],[0],[0],[0],[0], [], [], [],[0],[0],[0],[0],[0]]
    ]

    map = board(map1)

    print(map.current_loc(2))

    map.commit_move(current_loc=(3,9), new_loc=(3,10))
    
    print(map.current_loc(2))


    # print(board)
    #print(current_loc(1))
    #commit_move((9, 3), (9, 2))
    #print(board)
    # print(move(current_loc(1),'n', 1))

    #player_1 = valid_moves(current_loc(1), 3)
    #print(player_1)
    #print(current_loc(2))
    #player_2 = valid_moves(current_loc(2))
    #print(player_2)

    # path = shortest_path(start=current_loc(2),end=current_loc(1))
    # print(path)

    