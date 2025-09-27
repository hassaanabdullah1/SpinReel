from SpinReel import SpinReel
import random
sr = SpinReel()
icons = sr.icons
losses = 0
wins = 0
trials = 10_000_001
slots = 7
for x in range(trials):
        a = random.choices(icons, k=slots)
        if len(set(a)) == 1:
            wins += 1
        else:
            losses += 1

print(f"Wins: {wins}\tLosses: {losses}")

'''
I've already calculated some of the probabilities:
2 slots = wins: 1428728    losses: 8571273 
3 slots = wins: 203575     losses: 9796426
4 slots = wins: 29199      losses: 9970802
5 slots = wins: 4057       losses: 9995944
6 slots = wins: 605        losses: 9999396
7 slots = wins: 77         losses: 9999924
'''