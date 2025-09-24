import random
import math
import matplotlib.pyplot as plt


def runSession():
    sessionData = {
        "playerBalance": 100,
        "wonHands": 0,
        "wentBankrupt": False,
    }

    for _ in range(100):
        choice = random.choice(["win", "lose"])
        bet = math.ceil(sessionData["playerBalance"] * random.random())

        if choice == "win":
            sessionData["playerBalance"] += bet
            sessionData["wonHands"] += 1
        else:
            sessionData["playerBalance"] -= bet

        if sessionData["playerBalance"] <= 0:
            sessionData["wentBankrupt"] = True
            break

    return sessionData


def runSimulation(sessionCount=10000):
    totalWonHands = 0
    wonHandsCounts = []
    totalBankruptcies = 0

    for _ in range(sessionCount):
        sessionStats = runSession()

        totalWonHands += sessionStats["wonHands"]
        wonHandsCounts.append(sessionStats["wonHands"])

        if sessionStats["wentBankrupt"]:
            totalBankruptcies += 1

    print(f"Average won hands per session: {totalWonHands / sessionCount}")
    print(f"Total bankruptcies: {totalBankruptcies} out of {sessionCount} sessions")


runSimulation()
