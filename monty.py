import random

def monty_hall():
    prizes = [random.randint(1, 3) for _ in range(1000)]

    guesses = [random.randint(1, 3) for _ in range(1000)]

    x = set([1,2,3])

    removals = [list(x - set([prizes[i], guesses[i]])) for i in range(1000)]

    correct_wo_changing = sum(p == g for p, g in zip(prizes, guesses))

    correct_w_changing = 1000 - correct_wo_changing

    return (correct_wo_changing, correct_w_changing)

experiments = []

for i in range(1000):
    experiments.append(monty_hall())

no_switch_correct = sum(game[0] for game in experiments)
switch_correct = sum(game[1] for game in experiments)

print(f"Average times guesses were correct without switching after reveal {no_switch_correct/1000} i.e. {no_switch_correct/10}%")
print(f"Average times guesses were correct with switching after reveal {switch_correct/1000} i.e. {switch_correct/10}%")

