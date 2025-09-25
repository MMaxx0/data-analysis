import random
import matplotlib.pyplot as plt

session_length = 100  # Each session has 100 hands


def run_session():
    session_data = {
        "player_balance": 100,
        "won_hands": 0,
        "went_bankrupt": False,
        "hands_played": 0,
    }

    for _ in range(session_length):
        choice = random.choice(["win", "lose"])
        bet = 1

        if choice == "win":
            session_data["player_balance"] += bet
            session_data["won_hands"] += 1
        else:
            session_data["player_balance"] -= bet

        session_data["hands_played"] += 1

        if session_data["player_balance"] <= 0:
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
    n = total_hands_played  # sequence of n independent yes/no experiments
    n_per_session = session_length  # per session
    p = 0.5  # Probability of yes

    # Theoretical values
    # All hands considered values
    theoretical_expected_value = n * p
    theoretical_variance = n * p * (1 - p)
    # Per-session values (n=100 (session length), p=0.5)
    per_session_theoretical_expected_value = n_per_session * p  # 50
    per_session_theoretical_variance = n_per_session * p * (1 - p)  # 25
    # Bankruptcy
    per_session_bankruptcy_probability = (1 - p) ** n_per_session

    # Simulated variance
    mean_per_session = total_won_hands / session_count
    squared_diffs = [
        (session_wins - mean_per_session) ** 2 for session_wins in won_hands_counts
    ]
    per_session_variance = sum(squared_diffs) / (session_count - 1)
    simulated_variance = per_session_variance * session_count

    print(f"Total hands played: {total_hands_played}")
    print(f"Theoretical Expected value (hands won): {theoretical_expected_value}")
    print(f"Total hands won: {total_won_hands}")
    print(f"Theoretical variance: {theoretical_variance:.4f}")
    print(f"Simulated variance: {simulated_variance:.4f}")
    print(
        f"Probability of bankruptcy in a session: {per_session_bankruptcy_probability:.2e}"
    )
    print(f"Total bankruptcies: {total_bankruptcies} out of {session_count} sessions")

    # Plotting
    fig, axs = plt.subplots(2, 1, figsize=(12, 10))

    axs[0].bar(range(session_count), won_hands_counts, width=1)
    axs[0].set_xlabel("Session")
    axs[0].set_ylabel("Won Hands")
    axs[0].set_title("Won Hands per Session")
    theoretical_text = f"""**Theoretical Values**\nMean: {theoretical_expected_value:.4f}\nVariance: {theoretical_variance:.4f}\nBankruptcy probability: {per_session_bankruptcy_probability:.2e}"""
    simulated_text = f"""**Simulated Values**\nHands won: {total_won_hands:.4f}\nVariance: {simulated_variance:.4f}\nBankruptcies: {total_bankruptcies}"""
    add_stats_box(axs[0], 0.98, 0.98, theoretical_text, "#e0e0ff", "navy")
    add_stats_box(axs[0], 0.80, 0.98, simulated_text, "#ffe0e0", "darkred")
    axs[1].hist(
        won_hands_counts, bins="auto", color="skyblue", edgecolor="black", alpha=0.7
    )
    per_session_std_dev = per_session_variance**0.5

    axs[1].axvline(
        per_session_theoretical_expected_value,
        color="red",
        linestyle="dashed",
        linewidth=2,
        label="Theoretical Mean (per session)",
    )
    axs[1].axvline(
        mean_per_session + per_session_std_dev,
        color="green",
        linestyle="dotted",
        linewidth=2,
        label="+1 Std Dev",
    )
    axs[1].axvline(
        mean_per_session - per_session_std_dev,
        color="green",
        linestyle="dotted",
        linewidth=2,
        label="-1 Std Dev",
    )
    axs[1].set_xlabel("Won Hands per Session")
    axs[1].set_ylabel("Number of Sessions")
    axs[1].set_title("Distribution of Won Hands per Session")
    axs[1].grid(axis="y", linestyle="--", alpha=0.7)
    axs[1].legend()

    theoretical_per_session_text = f"""**Theoretical (Per Session)**\nMean: {per_session_theoretical_expected_value:.4f}\nVariance: {per_session_theoretical_variance:.4f}\nBankruptcy probability: {per_session_bankruptcy_probability:.2e}"""
    simulated_per_session_text = f"""**Simulated (Per Session)**\nMean: {mean_per_session:.4f}\nVariance: {per_session_variance:.4f}\nBankruptcies: {total_bankruptcies}"""

    add_stats_box(axs[1], 0.98, 0.98, theoretical_per_session_text, "#e0e0ff", "navy")
    add_stats_box(axs[1], 0.80, 0.98, simulated_per_session_text, "#ffe0e0", "darkred")
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
