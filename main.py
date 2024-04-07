
import random

adjectives = ["Cool", "Mystic", "Electric", "Wild", "Groovy"]

nouns = ["gmail"]

def generate_band_name():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adjective} {noun}"

band_name = generate_band_name()
band_name
