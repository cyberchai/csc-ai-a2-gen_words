import random

def gen(fsa):
    # given some fsa, we need to make sure we generate a valid word in the language
    word = ""
    current = "A"
    j = 0
    rand = 0

    while not(current in fsa[2] and rand > 6):
        if j >= len(fsa[1]):
            j = 0
        if fsa[1][j][0] == current:
            word = word + str(fsa[1][j][2])
            current = fsa[1][j][1]
            rand = random.randrange(0, 10, 1)
        j += 1
    return word


def main():
    states1 = ["A", "B", "C"]
    transitions1 = [["A", "B", 0], ["B", "C", 0], ["C", "B", 1]]
    final_states1 = ["B"]
    fsa1 = [states1, transitions1, final_states1]

    states2 = ["A", "B", "C", "D"]
    transitions2 = [["A", "B", 0], ["B", "C", 1], ["C", "D", 1], ["D", "B", 0], ["B", "B", 0]]
    final_states2 = ["B", "D"]
    fsa2 = [states2, transitions2, final_states2]


    print(gen(fsa2))

if __name__ == '__main__':
    main()
