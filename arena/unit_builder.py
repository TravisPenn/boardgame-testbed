import json

# create an instance of a Piece

def create_piece(pieces, tier, name):
    """
    
    :param pieces: json dictionary 
    :param tier: str, pieces[]
    :param name: str, pieces[][]
    :return: Piece class object
    """
    for u in pieces[tier]:
        if u.get("name") == name:
            #print(u)
            return Piece(tier, u)
        else:
            return "Piece not found"


class Piece:
    def __init__(self, tier, data):
        self.tier = tier
        self.name = data["name"]
        self.type = data["type"]
        self.health = data["health"]
        self.speed = data["speed"]
        self.defense_dice = data["defense_dice"]
        self.abilities = data["abilities"]
        self.status = []
        if tier == "hero" or tier == "hero_wounded":
            ## hero & hero_wounded
            self.endurance = data["endurance"]
            self.strength = data["strength"]
            self.insight = data["insight"]
            self.tech = data["tech"]
            self.strain = 0
            self.armor = []
            self.weapon = []
            self.equipment = []
        else:
            self.deployment_groups = data["deployment_groups"]
            self.reinforcement_cost = data["reinforcement_cost"]
            self.attack_dice = data["attack_dice"]
            self.attack_range = data["attack_range"]


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
    
    def stats(self):
        return []



if __name__ == "__main__":

    with open('../configs/pieces.json') as json_file:
        data = json.load(json_file)
    pieces = data["pieces"]

    with open('../configs/items.json') as json_file:
        items = json.load(json_file)

    equiped_weapon = next(item for item in items["weapons"] if item["name"] == "Plasteel Staff")

    #Piece = create_Piece(pieces, "standard", "Stormtrooper")
    #print(Piece.name, Piece.deployment_groups)

    Piece = create_piece(pieces, "hero", "Diala Passil")
    Piece.set_hero_weapon(equiped_weapon)
    print(Piece.name, Piece.weapon[0]["attack_type"])


