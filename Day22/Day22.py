from copy import deepcopy

startingDeck = []
second_startingDeck = []

with open("22.txt", "r") as f:
    parts = f.read().split("\n\n")

    startingDeck = [int(l) for l in parts[0].split("\n")[1:] if len(l) > 0]
    second_startingDeck = [int(l)
                           for l in parts[1].split("\n")[1:] if len(l) > 0]


def play(Deck1, Deck2):
    while len(Deck1) > 0 and len(Deck2) > 0:
        Card1 = Deck1.pop(0)
        Card2 = Deck2.pop(0)

        if Card1 > Card2:
            Deck1.extend([Card1, Card2])
        elif Card2 > Card1:
            Deck2.extend([Card2, Card1])

    return Deck1 if len(Deck1) > len(Deck2) else Deck2


Deck1 = deepcopy(startingDeck)
Deck2 = deepcopy(second_startingDeck)

deck = play(Deck1, Deck2)
n = len(deck)
points = [(n - i) * deck[i] for i in range(n)]

print(f"Q1: {sum(points)}")

n_games = 0
n_hits = 0


def _get(Deck1, Deck2):
    return tuple(Deck1 + [0] + Deck2)


def sol(Deck1, Deck2, back):
    global n_games
    global n_hits

    def before(Deck1, Deck2, back):
        hist_key = _get(Deck1, Deck2)

        if hist_key in back:
            return True

        back.add(hist_key)
        return False

    n_games += 1
    game = n_games

    n_rounds = 0
    finalAnswer = None

    while len(Deck1) > 0 and len(Deck2) > 0:
        n_rounds += 1
        if before(Deck1, Deck2, back):
            finalAnswer = (1, game, n_rounds, Deck1)
            n_hits += 1
            break
        else:
            Card1 = Deck1.pop(0)
            Card2 = Deck2.pop(0)

            if len(Deck1) >= Card1 and len(Deck2) >= Card2:
                rec_Deck1 = deepcopy(Deck1[:Card1])
                rec_Deck2 = deepcopy(Deck2[:Card2])

                answer = sol(rec_Deck1, rec_Deck2, set())
                won = answer[0]

                if won == 1:
                    Deck1.extend([Card1, Card2])
                else:
                    Deck2.extend([Card2, Card1])
            else:
                if Card1 > Card2:
                    Deck1.extend([Card1, Card2])
                elif Card2 > Card1:
                    Deck2.extend([Card2, Card1])

    if finalAnswer is None:
        finalAnswer = (1, game, n_rounds, Deck1) if len(
            Deck1) > len(Deck2) else (2, game, n_rounds, Deck2)

    return finalAnswer


Deck1 = deepcopy(startingDeck)
Deck2 = deepcopy(second_startingDeck)

back = set()
finalAnswer = sol(Deck1, Deck2, back)
deck = finalAnswer[-1]
n = len(deck)
points = [(n - i) * deck[i] for i in range(n)]

print(f"Q2: {sum(points)}")

back = list(back)
