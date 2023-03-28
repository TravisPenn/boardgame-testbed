from utilities import *
import os
import yaml
import json

# create an instance of a Piece

def create_piece(pieces, tier, name):
    """
    :param pieces: dir
    :param tier: str, pieces[]
    :param name: str, pieces[][]
    :return: Piece class object
    """
    if name in pieces.keys():
        return Piece(tier, pieces[name])


class Piece:
    def __init__(self, tier, data):
        self.tier = tier
        self.name = data["name"]
        self.type = data["type"]
        self.status = []
        if tier == "hero":
            self.strain = 0
            self.armor = []
            self.weapon = []
            self.equipment = []
            self.stats = {
                "health": data["base"]["health"],
                "speed" : data["base"]["speed"],
                "defense_dice" : data["base"]["defense_dice"],
                "abilities" : data["base"]["abilities"],
                "endurance" : data["base"]["endurance"],
                "strength" : data["base"]["strength"],
                "insight" : data["base"]["insight"],
                "tech" : data["base"]["tech"]
            }
            self.is_wounded = {
                "health": data["wounded"]["health"],
                "speed" : data["wounded"]["speed"],
                "defense_dice" : data["wounded"]["defense_dice"],
                "abilities" : data["wounded"]["abilities"],
                "endurance" : data["wounded"]["endurance"],
                "strength" : data["wounded"]["strength"],
                "insight" : data["wounded"]["insight"],
                "tech" : data["wounded"]["tech"]
            }
        else:
            self.attack_range = data["attack_range"]
            if tier == "standard" :
                self.stats = {
                    "deployment_groups" : data["standard"]["deployment_groups"],
                    "reinforcement_cost" : data["standard"]["reinforcement_cost"],
                    "attack_dice" : data["standard"]["attack_dice"],
                    "health" : data["standard"]["health"],
                    "speed" : data["standard"]["speed"],
                    "defense_dice" : data["standard"]["defense_dice"],
                    "abilities" : data["standard"]["abilities"]
                }
            if tier == "elite" :
                self.stats = {
                    "deployment_groups" : data["elite"]["deployment_groups"],
                    "reinforcement_cost" : data["elite"]["reinforcement_cost"],
                    "attack_dice" : data["elite"]["attack_dice"],
                    "health" : data["elite"]["health"],
                    "speed" : data["elite"]["speed"],
                    "defense_dice" : data["elite"]["defense_dice"],
                    "abilities" : data["elite"]["abilities"]
                }


    def __repr__(self):
        return yaml.dump(yaml.safe_load(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)))
    

    def set_hero_weapon(self, weapon):
        """
        Set hero's weapon
        """
        self.weapon.append(weapon)


    def set_hero_equipment(self, equipment):
        """
        Set hero's equipment
        """
        self.equipment.append(equipment)


    def set_hero_armor(self, armor):
        """
        Set hero's armor
        """
        self.armor.append(armor)
    
    # def stats(self):
    #     return []


if __name__ == "__main__":


    pieces, items, abilities = load_configs(selection=selection)
    #print(pieces)
    
    equiped_weapon = next(items[item] for item in items if items[item]["name"] == "Plasteel Staff")
    #print(equiped_weapon)
    
    # Piece = create_piece(pieces, "standard", "stormtrooper")
    # print(Piece.tier, Piece.name, Piece.stats)
    
    Piece = create_piece(pieces, "hero", "diala_passil")
    Piece.set_hero_weapon(equiped_weapon)
    #print(Piece.name, Piece.weapon[0], Piece.stats)
    print(Piece)

