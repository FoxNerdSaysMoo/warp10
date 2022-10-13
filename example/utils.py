import random

nameprefixes = [
    "Happy",
    "Sad",
    "Big",
    "Small",
    "Interesting",
    "Suspicious",
    "Strange",
    "Alienating",
    "Dreaded",
    "Livid",
    "Angry",
    "Enraged",
    "Stupid",
    "BigBrained",
    "Thin",
    "Thick",
    "Monstrous"
]

nameroots = [
    "Computer",
    "Person",
    "Koala",
    "Turtle",
    "Marmoset",
    "Orangutan",
    "Word",
    "Owl",
    "Fox",
    "Dog",
    "Cat",
    "Radio",
    "Mole",
    "Worm",
    "Insect",
    "Bee",
    "Pigeon",
    "Fish"
]

def random_name():
    return random.choice(nameprefixes) + random.choice(nameroots)
