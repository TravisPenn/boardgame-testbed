from ast import While
# from arena.mission_manager import mission_manager
from unit_builder import *
from dice_roller import *
from board import *
from actions import *
from display import *
import json

# Load Pieces
with open('../configs/pieces.json') as json_file:
    data = json.load(json_file)
pieces = data["units"]

# Load Items
with open('../configs/items.json') as json_file:
    items = json.load(json_file)

# Equip Units
equiped_weapon = next(item for item in items["weapons"] if item["name"] == "Plasteel Staff")

# Create Units for duel
Piece_1 = create_piece(pieces, "hero", "Diala Passil")
Piece_1.set_hero_weapon(equiped_weapon)

Piece_2 = create_piece(pieces, "elite", "Stormtrooper")

# Load Mission

# Create board
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


# load map and pieces into mission_manager()
#mission_manager.mission_manager(map=map, pieces=pieces, mission=mission)

# Setup board
map = board(map1)
pieces = [(1, Piece_1),(2, Piece_2)]

# Mission perams
    # Ending conditions
        # Round limit
        # Rewards

mission_threat = 3
threat = mission_threat
running = True
roundlimit = 3
roundcount = 1

# Start of Mission
# mission[round[activation]]

# List of avaiable Pieces on the map in alternating faction order
# List of completed Pieces

while running:
    print("-------------------------------------")
    print("Start of Round {0}".format(roundcount))
    print("-------------------------------------")

    # ready Piece.hero Class & Item cards
    display_map(map=map.board, map_name="Duel")
    # Round loop
    for piece in pieces:
        piece_location = piece[0]
        piece = piece[1]
        print("-------------------------------------")
        print("** {0}'s Turn **".format(piece.name))
        action_count = 2
        ## Build Action Pool
        if piece.tier == "hero" or piece.tier == "hero_wounded":
            action_pool = [
                'move', 'move',
                'attack', 'attack',
                'interact', 'interact',
                'rest', 'rest',
                'special','special'
            ]
        else:
            action_pool = [
                'move', 'move',
                'attack',
                'interact', 'interact',
                'special','special'
            ]

        ## activation phase
            # activation_triggers()
                # any of all Piece.abilities load in (e-web double attack, double move)

        for action in range(0, action_count):

            ## Select Actions from Pool
            print("Available Actions: {0}".format(action_pool))
            action = input('Select Action: ')

            if action in action_pool:
                action_pool.remove(action)
            else:
                print("Available Actions: {0}".format(action_pool))

            ## Execute Action
            if action == "move":
                move(map, piece, piece_location)
                #### movement pool
                # if move
                # init Piece speed
                # subtract from movement pool to move()

            if action == "attack":
                attack(map, piece, piece_location)

            if action == "interact":
                interact(map, piece, piece_location)

            if action == "rest":
                rest(piece)

            if action == "special":
                special(map, piece, piece_location)

    # End Mission
        # Ending conditions
        # Round limit
        # Rewards
    # TODO: break on health, break on goal
    if roundcount == roundlimit:
        print("-------------------------------------")
        print("Misson End: Round Limit Reached")
        print("-------------------------------------")
        running = False
        break    
# End of Round status phase
    # Increase Threat
    threat = mission_threat + threat
    # Ready
        # Imperial Class & Deployment cards
        # empty List of completed Pieces
    # Deploy and Reinforce
    # EndOfRound_Triggers()
    
    # Advance Round Dial
    roundcount += 1

# End of Mission
    # empty depleted list
    # empty defeated list
    # empty exhausted list
close_map()

