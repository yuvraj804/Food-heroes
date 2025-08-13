import random
from os.path import join, isfile

class superhero:
    instances = []

    def __init__(self, name, strength, dexterity, intelligence, tactic, catchphrase, location='unknown.jpeg'):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.tactic = tactic
        self.catchphrase = catchphrase
        self.average = (strength + dexterity + intelligence + tactic) / 4
        self.willcut = self.average > 80

        hero_path = join("Heroes", location)
        self.location = hero_path if isfile(hero_path) else join("Heroes", "unknown.jpeg")

        superhero.instances.append(self)

    @property
    def power(self):
        return self.average

    def WillCut(self):
        msg = [
            f"{self.name} is a certified superhero!",
            f"Of course {self.name} is a superhero!",
            f"Naturally, {self.name} qualifies as a superhero."
        ] if self.willcut else [
            f"Who is {self.name}?",
            f"I don't think {self.name} is a superhero!",
            f"I have never heard of {self.name}."
        ]
        print(random.choice(msg))

    def id(self):
        print(f"""
        Name: {self.name}
        Strength: {self.strength}
        Dexterity: {self.dexterity}
        Intelligence: {self.intelligence}
        Tactic: {self.tactic}
        Catchphrase: {self.catchphrase}
        """)

    def powerup(self, i=1):
        self.strength += i
        self.dexterity += i
        self.intelligence += i
        self.tactic += i
        self.average += i

    def weaken(self, i=1):
        self.strength -= i
        self.dexterity -= i
        self.intelligence -= i
        self.tactic -= i
        self.average -= i

    def draw_attribute(self):
        attributes = {
            'strength': self.strength,
            'dexterity': self.dexterity,
            'intelligence': self.intelligence,
            'tactic': self.tactic
        }
        key = random.choice(list(attributes.keys()))
        return key, attributes[key]
