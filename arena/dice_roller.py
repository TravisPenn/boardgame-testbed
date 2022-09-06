import json
import random
import re

def containsNumber(value):
    return bool(re.findall('[0-9]+', value))

def rollAllDice(dice: list) -> list:
    outcome = []
    with open('../configs/dice.json') as json_file:
        data = json.load(json_file)
    for die in dice:
        outcome.append((die, random.choice(data[die])))
    return outcome


def resolveSkillRoll(outcome: list) -> dict:
    results = {
        "total_surge": 0
    }
    for result in outcome:
        for ele in result[1]:
            if 'surge' in ele:
                results["total_surge"] += 1
    return results


def resolveAttackRoll(outcome: list) -> dict:
    """
    Attacker:
    Target:
    """
    results = {
        "total_surge": 0,
        "total_range": 0,
        "total_damage": 0,
        "total_evade": 0,
        "total_dodge": 0,
        "total_block": 0
    }
    for result in outcome:
        for ele in result[1]:
            if 'surge' in ele:
                results["total_surge"] += 1
            elif containsNumber(ele):
                num = int(ele)
                results["total_range"] += num
            elif 'damage' in ele:
                results["total_damage"] += 1
            elif 'evade' in ele:
                results["total_evade"] += 1
            elif 'block' in ele:
                results["total_block"] += 1
            elif 'dodge' in ele:
                results["total_dodge"] += 1

    # damage - block
    # print(results["total_damage"])
    results["total_damage"] = results["total_damage"] - results["total_block"]
    del results["total_block"]
    # surge - evade
    results["total_surge"] = results["total_surge"] - results["total_evade"]
    del results["total_evade"]
    # dodge = True

    # clean out 0 val keys
    # for k, v in results.items():
    #     if v == 0:
    #         del k 
    
    return results


if __name__ == "__main__":

    dice = ["blue","blue","green","white"]

    print("Attack/Def:")
    print(resolveAttackRoll(rollAllDice(dice)))

    print("Skill Check: New Roll..")
    print(resolveSkillRoll(rollAllDice(dice)))