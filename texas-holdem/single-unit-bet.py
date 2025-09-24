import random
import matplotlib.pyplot as plt


def run_session():
    session_data = {
        "player_balance": 100,
        "won_hands": 0,
        "went_bankrupt": False,
    }

    for _ in range(100):
        choice = random.choice(["win", "lose"])
        bet = 1

        if choice == "win":
            session_data["player_balance"] += bet
            session_data["won_hands"] += 1
        else:
            session_data["player_balance"] -= bet

        if session_data["player_balance"] <= 0:
            session_data["went_bankrupt"] = True
            break

    return session_data


def run_simulation(session_count=10000):
    total_won_hands = 0
    won_hands_counts = []
    total_bankruptcies = 0

    for _ in range(session_count):
        session_stats = run_session()

        total_won_hands += session_stats["won_hands"]
        won_hands_counts.append(session_stats["won_hands"])

        if session_stats["went_bankrupt"]:
            total_bankruptcies += 1

    average_won_hands = total_won_hands / session_count

    print(f"Average won hands per session: {average_won_hands}")
    print(f"Total bankruptcies: {total_bankruptcies} out of {session_count} sessions")
