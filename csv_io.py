import csv

import os
from superhero_class import superhero
from os.path import basename

def save_heroes_to_csv():
    filepath = "heroes.csv"

    unique_heroes = {}
    for hero in superhero.instances:
        unique_heroes[hero.name.lower()] = hero

    with open(filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "strength", "dexterity", "intelligence", "tactic", "catchphrase", "location"])

        for hero in unique_heroes.values():
            writer.writerow([
                hero.name,
                hero.strength,
                hero.dexterity,
                hero.intelligence,
                hero.tactic,
                hero.catchphrase,
                basename(hero.location)
            ])

def load_heroes_from_csv(filename="heroes.csv"):
    import csv
    superhero.instances = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                superhero(
                    name=row['name'],
                    strength=int(row['strength']),
                    dexterity=int(row['dexterity']),
                    intelligence=int(row['intelligence']),
                    tactic=int(row['tactic']),
                    catchphrase=row['catchphrase'],
                    location=row.get('location', 'unknown.jpeg')
                )
    except FileNotFoundError:
        print(f"{filename} not found. No heroes loaded.")


def register_fight_hero(hero, filename='fight_heroes.csv'):
    file_exists = os.path.isfile(filename)

    with open(filename, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Name', 'Strength', 'Dexterity', 'Intelligence', 'Tactic', 'Catchphrase',
                                               'Location'])

        if not file_exists or os.path.getsize(filename) == 0:
            writer.writeheader()

        writer.writerow({
            'Name': hero.name,
            'Strength': hero.strength,
            'Dexterity': hero.dexterity,
            'Intelligence': hero.intelligence,
            'Tactic': hero.tactic,
            'Catchphrase': hero.catchphrase,
            'Location': hero.location
        })

    print(f"[✔] {hero.name} registered for fight.")




import os
import csv
from superhero_class import superhero

def load_fight_heroes(index):
    file_path = 'fight_heroes.csv'

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for j, row in enumerate(reader):
            if j == index:
                location = os.path.normpath(row['Location'].strip())
                if not os.path.exists(location):
                    location = os.path.join("Heroes", "unknown.jpeg")

                return superhero(
                    name=row['Name'].strip(),
                    strength=int(row['Strength']),
                    dexterity=int(row['Dexterity']),
                    intelligence=int(row['Intelligence']),
                    tactic=int(row['Tactic']),
                    catchphrase=row['Catchphrase'].strip(),
                    location=location
                )

    return None
