import random
import matplotlib.pyplot as plt

session_length = 100  # Each session has 100 hands


def kelly_criterion(win_probability, win_proportion):
    bet_fraction = win_probability - ((1 - win_probability) / win_proportion)
    return bet_fraction


def run_session():
    session_data = {
        "player_balance": 100,
        "won_hands": 0,
        "went_bankrupt": False,
        "hands_played": 0,
    }

    win_probability = 0.5
    win_proportion = 2
    kelly_fraction = kelly_criterion(win_probability, win_proportion)

    for _ in range(session_length):
        choice = random.choice(["win", "lose"])
        bet = max(1, (kelly_fraction * session_data["player_balance"]))

        if choice == "win":
            session_data["player_balance"] += bet * win_proportion
            session_data["won_hands"] += 1
        else:
            session_data["player_balance"] -= bet

        session_data["hands_played"] += 1

        if session_data["player_balance"] < 1:
            session_data["went_bankrupt"] = True
            break

    return session_data


def run_simulation(session_count=10000):
    total_won_hands = 0
    total_hands_played = 0
    won_hands_counts = []
    total_bankruptcies = 0

    for _ in range(session_count):
        session_stats = run_session()

        total_won_hands += session_stats["won_hands"]
        total_hands_played += session_stats["hands_played"]
        won_hands_counts.append(session_stats["won_hands"])

        if session_stats["went_bankrupt"]:
            total_bankruptcies += 1

    # Following the Binomial distribution
    # Use actual average hands per session to account for bankruptcies
    n = total_hands_played / session_count  # actual average hands per session
    p = 0.5  # Probability of yes

    # Theoretical values
    per_session_theoretical_expected_value = n * p
    per_session_theoretical_variance = n * p * (1 - p)
    # Bankruptcy
    per_session_bankruptcy_probability = (1 - p) ** n

    # Simulated values
    mean_per_session = total_won_hands / session_count
    squared_diffs = [
        (session_wins - mean_per_session) ** 2 for session_wins in won_hands_counts
    ]
    per_session_variance = sum(squared_diffs) / (session_count - 1)

    print(f"Total hands played: {total_hands_played}")
    print(f"Theoretical Expected value: {per_session_theoretical_expected_value}")
    print(f"Total hands won: {total_won_hands}")
    print(f"Simulated Expected value: {mean_per_session:.4f}")
    print(f"Theoretical variance: {per_session_theoretical_variance:.4f}")
    print(f"Simulated variance: {per_session_variance:.4f}")
    print(
        f"Probability of bankruptcy in a session: {per_session_bankruptcy_probability:.2e}"
    )
    print(f"Total bankruptcies: {total_bankruptcies} out of {session_count} sessions")

    # Plotting
    fig, axs = plt.subplots(1, 1, figsize=(12, 10))

    axs.hist(
        won_hands_counts, bins="auto", color="skyblue", edgecolor="black", alpha=0.7
    )
    per_session_std_dev = per_session_variance**0.5

    axs.axvline(
        per_session_theoretical_expected_value,
        color="red",
        linestyle="dashed",
        linewidth=2,
        label="Theoretical Mean (per session)",
    )
    axs.axvline(
        mean_per_session + per_session_std_dev,
        color="green",
        linestyle="dotted",
        linewidth=2,
        label="+1 Std Dev",
    )
    axs.axvline(
        mean_per_session - per_session_std_dev,
        color="green",
        linestyle="dotted",
        linewidth=2,
        label="-1 Std Dev",
    )
    axs.set_xlabel("Won Hands per Session")
    axs.set_ylabel("Number of Sessions")
    axs.set_title("Distribution of Won Hands per Session")
    axs.grid(axis="y", linestyle="--", alpha=0.7)
    axs.legend()

    theoretical_per_session_text = f"""**Theoretical (Per Session)**\nMean: {per_session_theoretical_expected_value:.4f}\nVariance: {per_session_theoretical_variance:.4f}\nBankruptcy probability: {per_session_bankruptcy_probability:.2e}"""
    simulated_per_session_text = f"""**Simulated (Per Session)**\nMean: {mean_per_session:.4f}\nVariance: {per_session_variance:.4f}\nBankruptcies: {total_bankruptcies}"""

    add_stats_box(axs, 0.98, 0.98, theoretical_per_session_text, "#e0e0ff", "navy")
    add_stats_box(axs, 0.80, 0.98, simulated_per_session_text, "#ffe0e0", "darkred")
    plt.tight_layout()
    plt.show()


def add_stats_box(ax, x, y, text, color, edge):
    ax.text(
        x,
        y,
        text,
        transform=ax.transAxes,
        fontsize=10,
        va="top",
        ha="right",
        bbox=dict(boxstyle="round,pad=0.3", fc=color, ec=edge, lw=1),
    )


run_simulation()
