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

    # Following the Binomial distribution
    n = 100  # sequence of n independent yes/no experiments
    p = 0.5  # Probability of yes
    expected_value = n * p
    variance = n * p * (1 - p)
    total_bankruptcy_probability = (1 - p) ** n

    for _ in range(session_count):
        session_stats = run_session()

        total_won_hands += session_stats["won_hands"]
        won_hands_counts.append(session_stats["won_hands"])

        if session_stats["went_bankrupt"]:
            total_bankruptcies += 1

    average_won_hands = total_won_hands / session_count

    mean = sum(won_hands_counts) / len(won_hands_counts)
    squared_diffs = [(x - mean) ** 2 for x in won_hands_counts]
    simulated_variance = sum(squared_diffs) / (len(won_hands_counts) - 1)

    print(f"Average won hands per session: {average_won_hands}")
    print(f"Simulated variance: {simulated_variance:.4f}")
    print(f"Total bankruptcies: {total_bankruptcies} out of {session_count} sessions")
