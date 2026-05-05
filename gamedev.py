import random
import time

# classes
classes = {
    "1": {"name": "Warrior", "hp": 100, "atk": 12, "def": 8},
    "2": {"name": "Mage", "hp": 70, "atk": 15, "def": 4},
    "3": {"name": "Rogue", "hp": 80, "atk": 10, "def": 6}
}

# enemies
enemies = [
    {"name": "Goblin", "hp": 30, "atk": 6, "gold": 10},
    {"name": "Skeleton", "hp": 40, "atk": 8, "gold": 15},
    {"name": "Orc", "hp": 60, "atk": 10, "gold": 20},
    {"name": "Dweller", "hp": 80, "atk": 30, "gold": 50},
    {"name": "Shreak", "hp": 35, "atk": 15, "gold": 25},
    {"name": "Shade", "hp": 30, "atk": 20, "gold": 20}
]

#bosses
bosses = [
    {"name": "Crucible Knight", "hp": 150, "atk": 30, "gold": 100},
    {"name": "Rune Bear", "hp": 100, "atk": 40, "gold": 150},
    {"name": "Elden Beast", "hp": 500, "atk": 60, "gold": 300}
]

#shop
def shop(player):
    while True:
        print("\n=== SHOP ===")
        print(f"Gold: {player['gold']}")
        print("1. Heal Potion (+30 HP) - 15 gold")
        print("2. Attack Boost (+3 ATK) - 25 gold")
        print("3. Leave Shop")

        choice = input("> ")

        if choice == "1":
            if player["gold"] >= 15:
                player["gold"] -= 15
                player["hp"] += 30
                print("You used a potion. +30 HP!")
            else:
                print("Not enough gold.")

        elif choice == "2":
            if player["gold"] >= 25:
                player["gold"] -= 25
                player["atk"] += 3
                print("Attack increased!")
            else:
                print("Not enough gold.")

        elif choice == "3":
            break
        else:
            print("Invalid.")

#skills
def use_skill(player, enemy):
    if player["class"] == "Warrior":
        dmg = player["atk"] * 2
        print("Power Strike! Massive damage!")
    elif player["class"] == "Mage":
        dmg = player["atk"] + 10
        print("Fireball burns the enemy!")
    elif player["class"] == "Rogue":
        dmg = player["atk"] * random.choice([1, 2, 3])
        print("Critical Strike! Unpredictable damage!")
    else:
        dmg = player["atk"]

    enemy["hp"] -= dmg
    print(f"You dealt {dmg} damage!")

#battle system
def battle(player, enemy, is_boss=False):
    
    if is_boss:
        print(f"You now face the {enemy['name']}")

    else:
        print(f"\nA {enemy['name']} appears!")

    defending = False

    while enemy["hp"] > 0 and player["hp"] > 0:
        print(f"\nYour HP: {player['hp']} | {enemy['name']} HP: {enemy['hp']}")
        print("1. Attack")
        print("2. Defend")
        print("3. Skill")

        choice = input("> ")

        if choice == "1":
            dmg = max(0, player["atk"] - 2)
            enemy["hp"] -= dmg
            print(f"You dealt {dmg} damage!")

        elif choice == "2":
            defending = True
            print("You brace for impact!")

        elif choice == "3":
            use_skill(player, enemy)

        else:
            print("Invalid.")
            continue

        # Enemy turn
        if enemy["hp"] > 0:
            dmg = max(0, enemy["atk"] - player["def"])

            if defending:
                dmg //= 2
                defending = False
                print("Damage reduced!")

            player["hp"] -= dmg
            print(f"{enemy['name']} dealt {dmg} damage!")

    if player["hp"] > 0:
        print(f"\nYou defeated {enemy['name']}!")
        player["gold"] += enemy["gold"]
        print(f"You gained {enemy['gold']} gold!")
        return True
    else:
        print("\nYou were defeated...")
        return False


# game
def game():
    print("=== DUNGEON CRAWLER ===")

    name = input("Enter your name: ")

    print("\nChoose your class:")
    for key, c in classes.items():
        print(f"{key}. {c['name']} (HP:{c['hp']} ATK:{c['atk']} DEF:{c['def']})")

    choice = input("> ")
    chosen = classes.get(choice, classes["1"])

    player = {
        "name": name,
        "class": chosen["name"],
        "hp": chosen["hp"],
        "atk": chosen["atk"],
        "def": chosen["def"],
        "gold": 20
    }

    print(f"\nWelcome {player['name']} the {player['class']}!")

    # Dungeon stages
    for i in range(9):
        enemy = random.choice(enemies).copy()

        if not battle(player, enemy):
            print("\n=== GAME OVER ===")
            return

        shop(player)

    # FINAL BOSS
    final_boss = random.choice(bosses).copy()

    print(f"\nYou have reached the end of the dungeon...")

    if battle(player, final_boss, is_boss=True):
        print("\n=== YOU CLEARED THE DUNGEON! ===")
    else:
        print("\n=== GAME OVER ===")


game()