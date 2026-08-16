import random
import copy

running_game =  True


player = {
    "name": "tutle",
    "health": 250,
    "max_health": 300,
    "level":3,
    "base_damage": 30,
    "weapon_damage": 30,
    "damage": 60,
    "damage_boost_turns": 0,
    "gold": 500,
    "xp": 0,
    "xp_to_next_level": 100,
    "defense": 25,
    "equipped_weapon":"steel sword",
    "inventory":{
        "healing potion": 5,
        "damage potion": 3,
        "speed potion": 2,
        "double steel daggers": 1,
        "double steel swords": 1,
    },
    "equipped_armor": {
        "helmet_armor": {
            "name": "leather helmet armor",
            "defense_helmet": 5
        },
        "body_armor": {
            "name": "plastic body armor",
            "defense_body": 10
        },
        "leg_armor": {
            "name": "leather pants armor",
            "defense_leg": 5
        },
        "boots_armor": {
            "name": "steel boots armor",
            "defense_boots": 5
        }
    }
}
enemies = {
    "dragon" : {
    "name":"dragon",
    "health":135,
    "damage":65,
    "gold":130,
    "xp": 100,
    "drops": [
        "dragons teeth",
        "dragon heart",
        "dragon skin",
    ]
},

"baby_dragon" : {
    "name":"baby dragon",
    "health":95,
    "damage":25,
    "gold":55,
    "xp": 75,
    "drops": [
        "baby dragon heart",
        "baby dragon skin",
        "baby dragon eyes"
    ]
},

"slime" : {
    "name":"slime",
    "health":75,
    "damage":30,
    "gold":35,
    "xp": 50,
    "drops":[
        "slime goo",
        "slime heart",
    ]
},

"skeleton": {
    "name":"skeleton",
    "health":25,
    "damage":20,
    "gold":15,
    "xp": 25,
    "drops":[
        "skeleton_bone",
        "skeleton_rib",
        "skeleton_skull"
    ]
}


}

shop_weapons = {
    "dagger": {
        "name":"dagger",
        "damage": 15,
        "cost": 85,
        "description": "Tiny knife. Big confidence."

    },
    "long sword": {
        "name":"long sword",
        "damage": 35,
        "cost": 135,
        "description": "The classic 'hit it until it stops moving' weapon."
    },
    "rapier": {
        "name":"Rapier",
        "damage": 45,
        "cost": 150,
        "description": "The classic 'hit it until it stops moving' weapon."
    },
    "double steel daggers": {
        "name":"double steel daggers",
        "damage": 60,
        "cost": 200,
        "description": "Two daggers are better than one."
    },
    "double steel swords": {
        "name":"double steel swords",
        "damage": 80,
        "cost": 250,
        "description": "Two swords are better than one."
    },
    "broad sword": {
        "name": "broad sword",
        "damage": 50,
        "cost": 160,
        "description": "Swing once. Regret tomorrow."
    },
    "spear": {
        "name": "spear",
        "damage": 45,
        "cost": 120,
        "description": "Keeps monsters six feet away"
        },
    "morning star": {
        "name": "morning star",
        "damage": 90,
        "cost": 200,
        "description": "Dentist's worst nightmare."
        },
    "halberd": {
            "name": "halberd",
            "damage": 70,
            "cost": 180,
            "description": "Dentist's worst nightmare."
            }
}




shop_armor = {
    "helmet armor": {
        "plastic helmet armor": {
            "name": "plastic helmet armor",
            "defense_helmet": 5,
            "cost": 75,
            "description": "A plastic helmet that provides basic protection."
        },
        "leather helmet armor": {
            "name": "leather helmet armor",
            "defense_helmet": 10,
            "cost": 100,
            "description": "A leather helmet that provides moderate protection."
        },
        "steel helmet armor": {
            "name": "steel helmet armor",
            "defense_helmet": 15,
            "cost": 150,
            "description": "A steel helmet that provides excellent protection."
        },
        "iron helmet armor": {
            "name": "iron helmet armor",
            "defense_helmet": 20,
            "cost": 200,
            "description": "An iron helmet that provides great protection."
        }
    },
    "body armor": {
        "plastic body armor": {
            "name": "plastic body armor",
            "defense_body": 10,
            "cost": 100,
            "description": "A plastic body armor that provides basic protection."
        },
        "leather body armor": {
            "name": "leather body armor",
            "defense_body": 15,
            "cost": 150,
            "description": "A leather body armor that provides moderate protection."
        },
        "steel body armor": {
            "name": "steel body armor",
            "defense_body": 20,
            "cost": 200,
            "description": "A steel body armor that provides excellent protection."
        },
        "iron body armor": {
            "name": "iron body armor",
            "defense_body": 25,
            "cost": 250,
            "description": "An iron body armor that provides great protection."
        },
    },
    "leg armor": {
        "plastic leg armor": {
            "name": "plastic leg armor",
            "defense_leg": 5,
            "cost": 75,
            "description": "A plastic leg armor that provides basic protection."
        },
        "leather leg armor": {
            "name": "leather leg armor",
            "defense_leg": 10,
            "cost": 100,
            "description": "A leather leg armor that provides moderate protection."
        },
        "steel leg armor": {
            "name": "steel leg armor",
            "defense_leg": 15,
            "cost": 150,
            "description": "A steel leg armor that provides excellent protection."
        },
        "iron leg armor": {
            "name": "iron leg armor",
            "defense_leg": 20,
            "cost": 200,
            "description": "An iron leg armor that provides great protection."
        },
    },
    "boots armor": {
        "plastic boots armor": {
            "name": "plastic boots armor",
            "defense_boots": 5,
            "cost": 75,
            "description": "A plastic boots armor that provides basic protection."
        },
        "leather boots armor": {
            "name": "leather boots armor",
            "defense_boots": 10,
            "cost": 100,
            "description": "A leather boots armor that provides moderate protection."
        },
        "steel boots armor": {
            "name": "steel boots armor",
            "defense_boots": 15,
            "cost": 150,
            "description": "A steel boots armor that provides excellent protection."
        },
        "iron boots armor": {
            "name": "iron boots armor",
            "defense_boots": 20,
            "cost": 200,
            "description": "An iron boots armor that provides great protection."
        },
    }
}

quests = {
    "bone_to_pick":{
        "name": "ive got a  bone to pick",
        "description": "defeat 5 skeletons",
        "required":5,
        "progress":0,
        "target":"skeleton",
        "reward":{
            "gold":50,
            "xp": 35,
        },
    },
    "slimy":{
        "name": "its gonna get slimy",
        "description": "defeat 7 slimes",
        "required":7,
        "progress":0,
        "target":"slime",
        "reward":{
            "gold":85,
            "xp": 50,
        },
    },
    "beat_baby_dragons": {
        "name": "let's beat some baby dragon's, oh wait that seems weird",
        "description": "defeat 4 baby dragon",
        "required":4,
        "progress":0,
        "target":"baby dragon",
        "reward":{
           "gold":125,
            "xp": 85,
        },
    },
    "luckiest_monster":{
        "name": "MAN WHY IS DOES IT GATTA BE THE LUCKIESt MONSTER",
        "description": "defeat 3 dragon",
        "required":3,
        "progress":0,
        "target":"dragon",
        "reward":{
            "gold":175,
            "xp": 125,
       },
    }
}

potions = {
    "speed potion": {
        "name":"speed potion",
        "description":"it does nothing CUZ I HAVENT WRITEN THE CODE YET HAHAHAHAH",
        "cost":0
    },
    "healing potion": {
        "name":"healing potion",
        "description":"it heals you by 50 health",
        "cost":55
    },
    "damage potion": {
        "name": "damage potion",
        "description":" it increse damage by 3 turns",
        "cost":65
    }
}


def update_player_damage():
    player["damage"] = player["base_damage"] + player["weapon_damage"]


def update_player_defense():
    player["defense"] = player["equipped_armor"]["helmet_armor"]["defense_helmet"] + player["equipped_armor"]["body_armor"]["defense_body"] + player["equipped_armor"]["leg_armor"]["defense_leg"] + player["equipped_armor"]["boots_armor"]["defense_boots"]

def explore_button():
    spawn_chance = random.randint(1,10)

    if spawn_chance >= 7:
        current_enemy = copy.deepcopy(enemies["skeleton"])
    elif spawn_chance >= 4:
        current_enemy = copy.deepcopy(enemies["slime"])
    elif spawn_chance >= 2:
        current_enemy = copy.deepcopy(enemies["baby_dragon"])
    else:
        current_enemy = copy.deepcopy(enemies["dragon"])

    current_enemy["health"] = current_enemy["health"] + (player["level"] * 10)
    current_enemy["damage"] = current_enemy["damage"] + (player["level"] * 3)


    print("---------------------")
    print('')
    print(f"you found a {current_enemy['name']}!")
    print(f"damage: {current_enemy['damage']}")
    print(f"health: {current_enemy['health']}")
    print(f"gold: {current_enemy['gold']}")
    print('')
    print("---------------------")
    return current_enemy

def shop_menu():
    print("=================================")
    print("          TUTLES SHOP            ")
    print("=================================")
    print('')
    print("are your trying to buy, armor, weapons, or potions?")
    armor_or_weapons_or_potions = input("choose: ")
    if armor_or_weapons_or_potions == "weapons":
        for number, item in enumerate(shop_weapons, start=1):
            print(f"{number}. {shop_weapons[item]['name']}")
            print(f"damage: {shop_weapons[item]['damage']}")
            print(f"cost: {shop_weapons[item]['cost']}")
            print(f"description: {shop_weapons[item]['description']}")
            print('')
            print("---------------------------------")
        print("type the name of the item you would like to buy or type 'exit' to leave the shop")
        choose = input("choose: ")
        if choose == "exit":
            return
        elif choose in shop_weapons:
            if player["gold"] >= shop_weapons[choose]["cost"]:
                player["gold"] -= shop_weapons[choose]["cost"]
                weapon_name = shop_weapons[choose]["name"]
                if weapon_name in player["inventory"]:
                    player["inventory"][weapon_name] += 1
                else:
                    player["inventory"][weapon_name] = 1
                player["equipped_weapon"] = shop_weapons[choose]["name"]
                player["weapon_damage"] = shop_weapons[choose]["damage"]
                player["damage"] = player["base_damage"] + player["weapon_damage"]
                print(f"you have bought the {weapon_name}")
                print(f"you have equipped the {weapon_name}")
                print(f"your new damage is {player['damage']}")
            else:
                print("you dont have enough gold to buy this item")


    elif armor_or_weapons_or_potions == "armor":
        print("---------- choose -----------")
        print("1. helmet armor")
        print("2. body armor")
        print("3. leggings")
        print("4. boots")
        print("5. exit")
        choose_2 = input("choose :")
        if choose_2 == "exit" or choose_2 == "5":
            return
        elif choose_2 == "helmet armor" or choose_2 == "helmet" or choose_2 == "1":
            selected_armor = shop_armor["helmet armor"]
            armor_defense_type = "defense_helmet"
            armor_equipped = player["equipped_armor"]["helmet_armor"]
        elif choose_2 == "body armor" or choose_2 == "body" or choose_2 == "2":
            selected_armor = shop_armor["body armor"]
            armor_defense_type = "defense_body"
            armor_equipped = player["equipped_armor"]["body_armor"]
        elif choose_2 == "legging" or choose_2 == "3":
            selected_armor = shop_armor["leg armor"]
            armor_defense_type = "defense_leg"
            armor_equipped = player["equipped_armor"]["leg_armor"]
        elif choose_2 == "boots" or choose_2 == "4":
            selected_armor = shop_armor["boots armor"]
            armor_defense_type = "defense_boots"
            armor_equipped = player["equipped_armor"]["boots_armor"]

        else :
            print("type one of the following numbers")
            return

        for number, item in enumerate(selected_armor, start=1):
                    print(f"{number}. {selected_armor[item]['name']}")
                    print(f"defense: {selected_armor[item][armor_defense_type]}")
                    print(f"cost: {selected_armor[item]['cost']}")
                    print(f"description: {selected_armor[item]['description']}")


        choose_3 = input("what armor are you gonna buy ")
        print("only type in called armors okey cant do numbers sorry")

        if choose_3 == "exit":
            return

        if choose_3 in selected_armor:
            defense = selected_armor[choose_3][armor_defense_type]

            if player["gold"] >= selected_armor[choose_3]['cost']:
                player["gold"] -= selected_armor[choose_3]['cost']
                armor_name = selected_armor[choose_3]["name"]
                if armor_name in player["inventory"]:
                                player["inventory"][armor_name] += 1
                else:
                    player["inventory"][armor_name] = 1
                armor_equipped["name"] = armor_name
                armor_equipped[armor_defense_type] = defense
                update_player_defense()
                print(f"you have bought the {armor_name}")
                print(f"you have equipped the {armor_name}")
                print(f"your new defense is {armor_equipped[armor_defense_type]}")
            else :
                print(f"you dont have enough gold to buy {selected_armor[choose_3]['name']}")
    elif armor_or_weapons_or_potions == "potions":
        for number, item in enumerate(potions, start=1):
                            print(f"{number}. {potions[item]['name']}")
                            print(f"cost: {potions[item]['cost']}")
                            print(f"description: {potions[item]['description']}")
        potions_select = input("what potion do you want to buy ?")

        if potions_select == "1" or potions_select == "speed potion":
            if player["gold"] >= potions["speed potion"]["cost"]:
                player["gold"] -= potions["speed potion"]["cost"]
                potion_name = potions["speed potion"]["name"]
                if potion_name in player["inventory"]:
                    player["inventory"][potion_name] += 1
                else:
                    player["inventory"][potion_name] = 1
            else:
                print("you dont have enough gold")
                return
        elif potions_select == "2" or potions_select == "healing potion":
                    if player["gold"] >= potions["healing potion"]["cost"]:
                        player["gold"] -= potions["healing potion"]["cost"]
                        potion_name = potions["healing potion"]["name"]
                        if potion_name in player["inventory"]:
                            player["inventory"][potion_name] += 1
                        else:
                            player["inventory"][potion_name] = 1
                    else:
                        print("you dont have enough gold")
                        return
        elif potions_select == "3" or potions_select == "damage potion":
                    if player["gold"] >= potions["damage potion"]["cost"]:
                        player["gold"] -= potions["damage potion"]["cost"]
                        potion_name = potions["damage potion"]["name"]
                        if potion_name in player["inventory"]:
                            player["inventory"][potion_name] += 1
                        else:
                            player["inventory"][potion_name] = 1
                    else:
                        print("you dont have enough gold")
                        return
        else:
            return




def heal_menu():
    if player["inventory"].get('healing potion', 0) == 0:
        print("you dont have a healing potion")
        return

    if player["health"] >= player["max_health"]:
        print("you are already max health")
        return

    player["inventory"]["healing potion"] -= 1
    player["health"] += 50

    if player["health"] > player["max_health"]:
        player["health"] = player["max_health"]

    print("you have healed 50 hp")
    print(f"you health is now at {player['health']}/{player['max_health']}")


def view_stats_menu():
    print("=================================")
    print("               TUTLES STATS                ")
    print("=================================")
    print("")
    print("========== PLAYER ==========")
    print(f"name: {player['name']}")
    print(f"level: {player['level']}")
    print(f"health: {player['health']}/{player['max_health']}")
    print(f"damage: {player['damage']}")
    print(f"damage boost turns: {player['damage_boost_turns']}")
    print(f"xp: {player['xp']}/{player['xp_to_next_level']}")
    print(f"gold: {player['gold']}")
    print('')
    print('')
    print("weapon")
    print(f"{player['equipped_weapon']}")
    print('')
    print("\nInventory:")
    for item, quantity in player["inventory"].items():
        print(f"- {item}: {quantity}")
    print('')
    print('')
    print("\narmor")
    for armor_type, armor_data in player["equipped_armor"].items():
        print(f"- {armor_type}: {armor_data['name']}")

def calculation_damage_taken(enemy_damage):
    damage_taken = enemy_damage["damage"] - player["defense"]

    if damage_taken < 1:
            damage_taken = 1

    else:
        damage_taken

    player["health"] -= damage_taken

    return damage_taken


def inventory_menu():
    print("=================================")
    print("        TUTLES INVENTORY         ")
    print("=================================")
    print("")
    print("here is your items:")
    print("")
    for item, quantity in player["inventory"].items():
        print(f"- {item}: {quantity}")

    selecting = input("type the name of the item you would like to use or type 'exit' to leave the inventory: ")
    if selecting == "exit":
        return
    if selecting in player["inventory"] and player["inventory"][selecting] > 0:
        if selecting == "healing potion":
            heal_menu()
        elif selecting == "damage potion":
            player["inventory"]["damage potion"] -= 1
            player["damage_boost_turns"] += 3
            print("you have used a damage potion")
            update_player_damage()
        elif selecting == "speed potion":
            player["inventory"]["speed potion"] -= 1
            print("you have used a speed potion")
            print("it does nothing CUZ  I HAVENT WRITEN THE CODE YET HAHAHAHHAH")
        elif selecting in shop_armor:
            old_armor = player["equipped_armor"]
            player["equipped_armor"] = shop_armor[selecting]["name"]
            player["armor_defense"] = shop_armor[selecting]["defense"]
            update_player_defense()
            print(f"you have equipped the {shop_armor[selecting]['name']}")
            print(f"you have {player['damage_boost_turns']} turns of damage boost left")
        else:
            print("you cant use this item")


def combat_system(enemy_found):
    while player["health"] > 0 and enemy_found['health'] > 0:
        if player["health"] > 0:
            print("============= COMBAT MENU =============")
            print('')
            print(enemy_found["name"])
            print(f"health: {enemy_found['health']}")
            print('')
            print(f"your health: {player['health']}")
            print("")
            print("1. attack")
            print("2. heal")
            print("3. bail")
            print('')
            choice = input("choose: ")
            print("")
            if choice == "1" or choice == "attack":
                damage = player["damage"]

                if player["damage_boost_turns"] > 0:
                    damage += 10
                    player["damage_boost_turns"] -= 1

                enemy_found["health"] -= damage

                print(f"you hit the {enemy_found['name']} ")
                print(f"the enemies health is now at {enemy_found['health']}")
            elif choice == "2" or choice == "heal":
                heal_menu()
            elif choice == "3" or choice == "bail":
                print("you ran away!")
                return
            else:
                print("plz type one of the following numbers")
        else:
            print("WASTED")

        if enemy_found["health"] <= 0:
            print(f"the {enemy_found['name']} is dead")
            giving_loot(enemy_found)

            return

        if enemy_found["health"] > 0:
            print(f"the {enemy_found['name']} attacks!!")

            damage_taken = calculation_damage_taken(enemy_found)
            print(f"you took {damage_taken} damage")
            print(f"your health is now at {player['health']}")
        else:
            print("the enemy is dead")
            giving_loot(enemy_found)

def quest_randomizer():
    quest_name = random.choice(list(quests.keys()))
    active_quest = copy.deepcopy(quests[quest_name])
    return active_quest

active_quest = quest_randomizer()

def quest_viewing():
    print("===================================")
    print("       MIKEY THE QUEST GIVER          ")
    print("===================================")
    print('')
    print('')
    print("your quest is")
    print(f"name: {active_quest['name']}")
    print(f"description: {active_quest['description']}")
    print(f"progress: {active_quest['progress']}/{active_quest['required']}")


def quest_system(enemy_found,active_quest):

    if enemy_found["name"] == active_quest["target"]:
        active_quest["progress"] += 1
        if active_quest["progress"] >= active_quest["required"]:
            player["gold"] += active_quest['reward']['gold']
            player['xp'] += active_quest['reward']['xp']
            print("congrats the quest is done heres")
            print(f"gold: {active_quest['reward']['gold']}")
            print(f"xp: {active_quest['reward']['xp']}")
            level_up_system()
            return quest_randomizer()
    return active_quest


def giving_loot(enemy_found):
    drop = random.choice (enemy_found["drops"])
    print(f"congrats you defeated the {enemy_found['name']}")
    print(f"'gives player {enemy_found['gold']} gold and {drop}'")
    player["gold"] += enemy_found["gold"]
    player["xp"] += enemy_found["xp"]
    if drop in player["inventory"]:
        player["inventory"][drop] += 1
    else:
        player["inventory"][drop] = 1
    level_up_system()
    global active_quest
    active_quest = quest_system(enemy_found,active_quest)


def menu():
    print("---------------------------------------------")
    print("       WELCOME TO TUTLES GAME        ")
    print("---------------------------------------------")
    print("1. explore")
    print("2. heal menu")
    print("3. see stats")
    print("4. inventory")
    print("5. shop")
    print("6. quest")
    print("7. quit")
    selecting = input("select one of the following numbers or name ")
    if selecting == "1" or selecting == "explore":
        enemy_found = explore_button()
        combat_system(enemy_found)
    elif selecting == "2" or selecting == "heal":
        heal_menu()
    elif selecting == "3" or selecting == "stats":
        view_stats_menu()
    elif selecting == "4" or selecting == "inventory":
        inventory_menu()
    elif selecting == "5" or selecting == "shop":
        shop_menu()
    elif selecting == "6" or selecting =="quest":
        quest_viewing()
    elif selecting == "7" or selecting == "quit":
        global running_game
        running_game = False
    else:
        print("plz type one of the following numbers")

def level_up_system():
    while player["xp"] >= player["xp_to_next_level"]:
        player["level"] += 1
        player["max_health"] += 50
        player["health"] = player["max_health"]
        player["base_damage"] += 10
        update_player_damage()
        player["xp"] -= player["xp_to_next_level"]
        player["xp_to_next_level"] = int(player["xp_to_next_level"] * 1.5)
        print(f"congrats you leveled up to level {player['level']}")
        print(f"you need {player['xp_to_next_level']} xp to reach the next level")
    else:
        return

while running_game:
    menu()
