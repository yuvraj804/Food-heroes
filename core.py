
from csv_io import save_heroes_to_csv
from superhero_class import superhero
def create_default_heroes():
    Batman = superhero(
        'Burgernaut', 95, 70, 80, 85,
        "Ketchup, mustard… and mayhem!",
        "Burgernaut.jpeg"
    )
    # ➤ Strong tank-type hero; high strength, average tactics.

    Superman = superhero(
        'Super Sandwich', 88, 85, 90, 86,
        "Fear the footlong of justice!",
        "supersandwich.jpeg"
    )
    # ➤ Balanced all-rounder.

    Flash = superhero(
        'Tactical Taco', 72, 98, 84, 91,
        "Every mission... fully loaded.",
        "tacticaltaco.jpeg"
    )
    # ➤ Super agile tactician.

    GreenLantern = superhero(
        'Captain Ketchup', 78, 82, 85, 95,
        "Time to ketchup with justice!",
        "captainketchup.jpeg"
    )
    # ➤ Commanding presence; top-tier tactical mind.

    WonderWoman = superhero(
        'Nacho Ninja', 80, 97, 90, 89,
        "I crunch in the shadows!",
        "nachoninja.jpeg"
    )
    # ➤ Ninja reflexes, sharp intellect, skilled tactician.

    Aquaman = superhero(
        'Practical Pizza', 75, 82, 98, 93,
        "Thin crust, thick strategy",
        "practicalpizza.jpeg"
    )
    # ➤ Extremely smart and strategic.

    Cyborg = superhero(
        'Surgical Smoothie', 79, 90, 92, 87,
        "Smooth. Sharp. Surgical.",
        "surgicalsmoothie.jpeg"
    )
    # ➤ High-tech brain and smooth execution.

    MartianManhunter = superhero(
        'Furious Fries', 94, 92, 76, 88,
        "You just got deep-fried!",
        "furiousfries.jpeg"
    )
    # ➤ Intense power and speed, decent tactical skills.

    save_heroes_to_csv()


def Name():
    for hero in superhero.instances:
        print(hero.name)


def fight(hero1, hero2):
    print(f"\n{hero1.name} vs {hero2.name}!")

    attr1, val1 = hero1.draw_attribute()
    attr2, val2 = hero2.draw_attribute()

    print(f"{hero1.name} draws {attr1.upper()} = {val1}")
    print(f"{hero2.name} draws {attr2.upper()} = {val2}")

    if val1 > val2:
        print(f"\n🏆 {hero1.name} wins the battle!\n")
    elif val2 > val1:
        print(f"\n🏆 {hero2.name} wins the battle!\n")
    else:
        print("\n⚔️ It's a tie!\n")


def destroy_hero(name):
    for hero in superhero.instances:
        if hero.name.lower() == name.lower():
            superhero.instances.remove(hero)
            print(f"❌ {hero.name} has been destroyed.")
            return
    print("Hero not found.")

create_default_heroes()