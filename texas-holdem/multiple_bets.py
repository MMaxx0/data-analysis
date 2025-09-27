import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Possible results and probabilities
outcomes = np.array([1, -5, 5, -100])   
probs = np.array([0.70, 0.10, 0.15, 0.05])

def session(hands=100, player_1=100, player_2=100):
    stack_p1 = player_1
    stack_p2 = player_2
    historial_p1 = [stack_p1]
    historial_p2 = [stack_p2]

    bankruptcy = False
    wins_p1 = 0
    wins_p2 = 0

    for _ in range(hands):
        change = np.random.choice(outcomes, p=probs)
        if (change > 0): 
            if change == outcomes[-1]: 
                change = min(stack_p1, stack_p2)
            stack_p1 += change
            stack_p2 -= change 
            wins_p1 += 1
        else: 
            stack_p1 += change
            stack_p2 -= change
            wins_p2 += 1
        historial_p1.append(stack_p1)
        historial_p2.append(stack_p2)
        outcomes[-1] = stack_p1
        
        if stack_p1 <= 0 or stack_p2 <= 0:  
            bankruptcy = True   
            break
    return(wins_p1, wins_p2, bankruptcy)

# Simulation
num_sessions = 10000
wins_p1_list = []
wins_p2_list = []
total_wins_p1 = 0
total_wins_p2 = 0
bankruptcy_count = 0  

for _ in range(num_sessions): 
    wins_p1, wins_p2, bankruptcy = session()
    wins_p1_list.append(wins_p1)
    wins_p2_list.append(wins_p2)
    total_wins_p1 += wins_p1
    total_wins_p2 += wins_p2

    if bankruptcy:
        bankruptcy_count += 1


wins_p1_arr = np.array(wins_p1_list)
wins_p2_arr = np.array(wins_p2_list)

handsplayed = total_wins_p1 + total_wins_p2

print(f"\nTotal wins across {handsplayed} hands (10000 sessions):")
print("Player 1:", total_wins_p1)
print("Player 2:", total_wins_p2)
print(f"\nAmount of sessions ended by bankruptcy: {bankruptcy_count}")
print(f"Bankruptcy propotion: {bankruptcy_count/num_sessions:.2%}")

expected_p1 = total_wins_p1 / handsplayed
expected_p2 = total_wins_p2 / handsplayed

# Conversion of expected values per hand, for variance.
p1_per_hand_session = np.array([w / (w + l) for w, l in zip(wins_p1_list, wins_p2_list)])
p2_per_hand_session = np.array([w / (w + l) for w, l in zip(wins_p2_list, wins_p1_list)])

var_p1 = np.var(p1_per_hand_session, ddof=1)
var_p2 = np.var(p2_per_hand_session, ddof=1)

print("\nExpected probability of winning a hand:")
print("Player 1:", expected_p1)
print("Player 2:", expected_p2)

print("\nVariance of wins per hand:")
print("Player 1:", var_p1)
print("Player 2:", var_p2)

# --- 1) Hands won per session ---
plt.figure(figsize=(12, 6))
plt.plot(wins_p1_arr, label='Player 1', alpha=0.6)
plt.plot(wins_p2_arr, label='Player 2', alpha=0.6)
plt.xlabel("Session")
plt.ylabel("Hands won")
plt.title("Hands won per session for each player")
plt.legend()
plt.show()

# --- 2) Expected value for each player ---
plt.figure(figsize=(8, 6))
plt.bar(['Player 1', 'Player 2'], [expected_p1, expected_p2], color=['blue', 'orange'])
plt.ylabel("Expected probability of winning a hand")
plt.title("Expected value per hand for each player")
plt.show()

#  --- 3) Histogram distribution plot ---
# Option B (recommended): histograms in counts + scaled theoretical pdf for Player 1
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Player 1 counts histogram
counts, bins, _ = axs[0].hist(wins_p1_arr, bins="auto", color="skyblue",
                              edgecolor="black", alpha=0.7)
bin_width = bins[1] - bins[0]

# Scale the pdf so area under pdf matches total count * bin_width -> pdf*len*bin_width -> counts scale
x = np.linspace(0, wins_p1_arr.max(), 500)
mu = 5.95
sigma = np.sqrt(471.5475)
pdf = norm.pdf(x, mu, sigma)
scaled_pdf = pdf * len(wins_p1_arr) * bin_width

axs[0].plot(x, scaled_pdf, "r-", lw=2, label="Theoretical Normal (scaled)")
axs[0].axvline(np.mean(wins_p1_arr), color="red", linestyle="dashed", linewidth=2, label="Sim Mean")
axs[0].axvline(np.mean(wins_p1_arr) + np.std(wins_p1_arr), color="green", linestyle="dotted", linewidth=2, label="+1 Std Dev")
axs[0].axvline(np.mean(wins_p1_arr) - np.std(wins_p1_arr), color="green", linestyle="dotted", linewidth=2, label="-1 Std Dev")
axs[0].set_title("Distribution of Wins per Session (Player 1)")
axs[0].set_xlabel("Hands Won")
axs[0].set_ylabel("Number of Sessions")
axs[0].legend()
axs[0].grid(axis="y", linestyle="--", alpha=0.7)

# Player 2 counts histogram (keep counts)
axs[1].hist(wins_p2_arr, bins="auto", color="orange", edgecolor="black", alpha=0.7)
axs[1].axvline(np.mean(wins_p2_arr), color="red", linestyle="dashed", linewidth=2, label="Sim Mean")
axs[1].axvline(np.mean(wins_p2_arr) + np.std(wins_p2_arr), color="green", linestyle="dotted", linewidth=2, label="+1 Std Dev")
axs[1].axvline(np.mean(wins_p2_arr) - np.std(wins_p2_arr), color="green", linestyle="dotted", linewidth=2, label="-1 Std Dev")
axs[1].set_title("Distribution of Wins per Session (Player 2)")
axs[1].set_xlabel("Hands Won")
axs[1].legend()
axs[1].grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show()
