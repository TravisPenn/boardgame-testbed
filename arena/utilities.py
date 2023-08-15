import yaml
import os

selection = {
    "pieces": ["diala_passil", "stormtrooper"],
    "items": {
        "weapons": ["plasteel_staff", "infantry_rifle"],
        "armor": ["black_sun_armor"]
    },
    "abilities": ["foresight", "precise_strike"]
}


def load_configs(selection):
    pieces = {}
    items = {}
    abilities = {}

    for i in selection.keys():
        if "pieces" in selection.keys():
            for j in selection["pieces"]:
                with open('../configs/pieces/{}.yaml'.format(j)) as file:
                    data = yaml.safe_load(file)
                    pieces[j] = data
        if "items" in selection.keys():
            for j in selection["items"]:
                for k in selection["items"][j]:
                    with open('../configs/items/{}/{}.yaml'.format(j,k)) as file:
                        data = yaml.safe_load(file)
                        items[k] = data
        if "abilities" in selection.keys():
            for j in selection["abilities"]:
                with open('../configs/abilities/{}.yaml'.format(j)) as file:
                    data = yaml.safe_load(file)
                    abilities[j] = data
    return pieces, items, abilities


def import_yaml_files(directory):
    """
    Recursively import all YAML files in a directory and its subdirectories.
    
    Parameters:
    directory (str): Path to the directory to search for YAML files.
    
    Returns:
    dict: A dictionary containing the YAML data, with keys based on the file names and paths.
    """
    yaml_data = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.yaml') or filename.endswith('.yml'):
                filepath = os.path.join(root, filename)
                with open(filepath) as file:
                    name = filepath.rsplit('/')[-2]
                    yaml_data.setdefault(name,[]).append(yaml.safe_load(file))
    return yaml_data



if __name__ == "__main__":

    pieces, items, abilities = load_configs(selection=selection)
    print(pieces)

    # for item in items:
    #     print(items[item])

    eq =  next(items[item] for item in items if items[item]["name"] == "Plasteel Staff")

    #print(eq)
