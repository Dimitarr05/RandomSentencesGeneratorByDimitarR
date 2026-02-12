import random

def get_random_word(words):
    return random.choice(words)

names = ["Ivan", "Georgi", "Petar", "Dimitar"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas", "Stara Zagora"]
verbs = ["jumps over", "throws", "catches", "builds", "breaks"]
nouns = ["books", "pizza", "phone", "ball", "flowers"]
adverbs = ["happily", "quietly", "bravely", "carefully", "eagerly"]
details = ["near the supermarket", "at home", "in the park", "at school"]

while 1:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)

    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}.")

    input("Click [Enter] to generate a new one.")