def Mystery():
    import random
    from superhero_class import superhero

    adjectives = [
        "Spicy", "Zesty", "Crispy", "Cheesy", "Flaming", "Greasy",
        "Icy", "Sticky", "Sizzling", "Bold", "Crunchy", "Toasty",
        "Furious", "Flaky", "Tangy", "Saucy", "Savory", "Swift", "Surgical"
    ]

    fast_foods = [
        "Burger", "Fries", "Pizza", "Nugget", "Donut", "Taco",
        "Hotdog", "Sandwich", "Wrap", "Drumstick", "Shake", "Sub",
        "Burrito", "OnionRing"
    ]


    adj = random.choice(adjectives)
    food = random.choice(fast_foods)
    name = f"{adj} {food}"


    catchphrases = [
        f"When the heat's on, the {name} brings the crunch!",
        f"You can’t escape the {name}!",
        f"Justice is best served spicy and wrapped – like the {name}!",
        f"Feel the wrath of the {name}!",
        f"One bite and you're toast – courtesy of the {name}!",
        f"The {name} never backs down!",
        f"I'm the {name} – and you're stuck with me!",
        f"Fear the fury of the {name}!",
        f"I bring the fight, deep-fried and dangerous – I’m the {name}!",
        f"The {name} strikes again – with extra vengeance!",
        f"Cool as an {name}, deadly as ever.",
        f"The {name} bites back!",
        f"The {name} oozes justice!",
        f"You just crossed the {name} – prepare to cry!",
        f"My justice drips with flavor – I’m the {name}!",
        f"Foes fall before the {name}!",
        f"From the fryer to the frontline – I fight for flavor!",
        f"Mess with the {name}, and you're glazed!",
        f"The battle's heating up – time for the {name}!",
        f"Sauce, speed, and strength – that's the {name} combo!"
    ]
    catchphrase = random.choice(catchphrases)


    strength = random.randint(60, 100)
    dexterity = random.randint(60, 100)
    intelligence = random.randint(60, 100)
    tactic = random.randint(60, 100)


    mystery_hero = superhero(
        name=name,
        strength=strength,
        dexterity=dexterity,
        intelligence=intelligence,
        tactic=tactic,
        catchphrase=catchphrase,
        location='unknown.jpeg'
    )

    print(f"Mystery Hero Created: {mystery_hero.name} — {mystery_hero.catchphrase}")
    return mystery_hero
