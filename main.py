import random

"""
Chaira, Juniper, Glory
A2 for CSC 290. October 2024.
"""

"""
generate a singular word
"""
def gen(fsa):
    # empty word to begin with
    word = ""
    # for the random length of a word
    rand = 0
    # counts how many times this function swaps between consonants and vowel sounds.
    counter = 0

    # this randomly chooses if a word starts with a consonant or not, with a bias toward consonant starts to reflect the english langauge (from what I/we think)
    # 65% more likely for generated words to start with a consonant
    # is_consonant = random.choice([True, False])
    is_consonant = random.choices([True, False], weights=[65, 35])[0]

    # while not(current in fsa[2] and rand > 7):
    #     if j >= len(fsa[1]):
    #         j = 0
    #     if fsa[1][j][0] == current:
    #         word = word + str(fsa[1][j][2])
    #         current = fsa[1][j][1]
    #         rand = random.randrange(0, 10, 1)
    #     j += 1

    # this determines the first letter(s)/start of the word
    # current_letter = random.choice(fsa[is_consonant].keys())
    current_letter = random.choice(list(fsa[is_consonant].keys()))
    word += current_letter
    counter += 1

    # our conditions for adding letters/compound letters:
    # 1. the letter is not an accept state (cannot end on letter)
    # 2. we need to have at least one vowel and at least one consonant in our word
    # 3. the random length assigned has not been satisfied

    # while not(fsa[is_consonant][current_letter]) and len(word) <= rand_word_len:
    while len(word) < 3 or not fsa[is_consonant][current_letter]:
        is_consonant = not is_consonant
        current_letter = random.choice(list(fsa[is_consonant].keys()))
        word += current_letter

        if len(word) >= 3 and fsa[is_consonant][current_letter]:
            break

    return word


"""
generate some specified number of words, num_words
"""
def gen_words(words_fsa, num_words):
    for i in range(num_words):
        print(gen(words_fsa))


"""
main method
"""
def main():
        # vowel sounds -- True corresponds to being a final state
    vowels = {
        "a": True,
        "e": True,
        "i": False,
        "o": False,
        "u": False,
        "oo": False,
        "ow": True,
        "oe": True,
        "ou": False,
        "oa": False,
        "ai": False,
        "ie": True,
        "ei": False,
    }

    # consonant sounds -- True corresponds to being a final state
    # discluded nk, ck, rk, ng, and ss because they can't start a word -- we can modify our datastructure to improve this.
    cons = {
        "b": True,
        "c": False,
        "d": True,
        "f": True,
        "g": True,
        "h": False,
        "j": False,
        "k": False,
        "l": True,
        "m": True,
        "n": True,
        "p": True,
        "q": False,
        "r": True,
        "s": False,
        "t": True,
        "v": True,
        "w": True,
        "x": True,
        "y": True,
        "z": True,
        "th": True,
        "sh": True,
        "ch": True,
        "ph": True,
        "wh": False,
        "cr": False,
        "pr": False,
        "tr": False,
        "dr": False,
        "fr": False,
        "gr": False,
        "br": False,
        "qu": False,
        "cl": False,
        "fl": False,
        "pl": False,
        "sl": False,
        "bl": False,
        "tw": False,
        "cy": False,
        "es": True
    }

    words_fsa = [vowels, cons]

    gen_words(words_fsa, 10)

"""
run main
"""
if __name__ == '__main__':
    main()
