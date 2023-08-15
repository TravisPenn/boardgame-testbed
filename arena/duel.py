from ast import While
# from arena.mission_manager import mission_manager
from unit_builder import *
from dice_roller import *
from board import *
from actions import *
from display import *
from utilities import *
import json
  

# Load configs ############################
selection = {
    "pieces": ["diala_passil", "stormtrooper"],
    "items": {
        "weapons": ["plasteel_staff", "infantry_rifle"],
        "armor": ["black_sun_armor"]
    },
    "abilities": ["foresight", "precise_strike"]
}

pieces, items, abilities = load_configs(selection=selection)

#########################################

# Equip Units
equiped_weapon = next(items[item] for item in items if items[item]["name"] == "Plasteel Staff")

# Create Units for duel
Piece_1 = create_piece(pieces, "hero", "hero", "diala_passil")
Piece_1.set_hero_weapon(equiped_weapon)

Piece_2 = create_piece(pieces, "nonhero", "elite", "stormtrooper")

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
    [[0], [], [3], [2],[], [], [], [], [], [], [], [],[0]],
    [[0],[0], [], [], [4], [], [], [], [], [], [],[0],[0]],
    [[0],[0],[0], [], [], [], [], [], [], [],[0],[0],[0]],
    [[0],[0],[0],[0],[0], [], [], [],[0],[0],[0],[0],[0]]
]


# load map and pieces into mission_manager()
#mission_manager.mission_manager(map=map, pieces=pieces, mission=mission)

# Setup board
map = board(map1)
pieces = [(1, Piece_1),(2, Piece_2),(3, Piece_2),(4, Piece_2)]

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
    
    map_name="Duel"
    # ready Piece.hero Class & Item cards
    display_map(map=map.board, map_name=map_name)
    # Round loop
    for piece in pieces:
        piece_map_id = piece[0]
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
                # map, piece = 
                move(map, piece, piece_map_id)
                #### movement pool
                # if move
                # init Piece speed
                # subtract from movement pool to move()

            if action == "attack":
                attack(map, piece, piece_map_id) # need dice

            if action == "interact":
                interact(map, piece, piece_map_id) # need dice

            if action == "rest":
                rest(piece)

            if action == "special":
                special(map, piece, piece_map_id)

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

