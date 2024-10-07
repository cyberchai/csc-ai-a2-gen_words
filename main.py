import random

def gen(fsa):
    # given some fsa, we need to make sure we generate a valid word in the language
    word = ""
    current = "A"
    j = 0
    rand = 0

    while not(current in fsa[2] and rand > 8):
        if j >= len(fsa[1]):
            j = 0
        if fsa[1][j][0] == current:
            word = word + str(fsa[1][j][2])
            current = fsa[1][j][1]
            rand = random.randrange(0, 10, 1)
        j += 1
    return word


def main():
    vowels = [["a", True], ["e", True], ["i", False], ["o", False], ["u", False], ["oo", False], ["ow", True], ["oe", True], ["ou", False], ["oa", False], ["ai", True], ["ie", True], ["ei", False]]
    cons = [["b", True], ["c", False], ["d", True], ["f", True], ["g", True], ["h", False], ["j", False], ["k", False], ["l", True], ["m", True], ["n", True], ["p", True], ["q", False], ["r", True], ["s", False], ["t", True], ["v", True], ["w", True], ["x", True], ["y", True], ["z", True]]
    states1 = [vowels, cons]

    transitions1 = [[vowels, cons, random.choise(cons)], [cons, vowels, vowels]]
    final_states1 = ["B"]
    words_fsa = [states1, transitions1, final_states1]


    print(gen(fsa2))

if __name__ == '__main__':
    main()
