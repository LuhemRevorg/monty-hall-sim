# Monty Hall Simulation

A Python simulation of the Monty Hall problem, demonstrating why switching doors is the optimal strategy.

## The Problem

The Monty Hall problem is a probability puzzle:

1. There are 3 doors — behind one is a prize, behind the others are nothing.
2. You pick a door.
3. The host (who knows what's behind each door) opens one of the other doors, revealing no prize.
4. You're given the choice to stick with your original pick or switch to the remaining door.

Counterintuitively, **switching wins 2/3 of the time**.

## How It Works

The simulation runs 1,000 games per experiment across 1,000 experiments (1,000,000 total games):

- Prizes and initial guesses are randomly assigned.
- The host's reveal is simulated by computing which door can be safely removed.
- Results are tallied for both strategies: **stay** and **switch**.

## Running

```bash
python monty.py
```

## Example Output

```
Average times guesses were correct without switching after reveal 334.495 i.e. 33449.5%
Average times guesses were correct with switching after reveal 665.505 i.e. 66550.5%
```
