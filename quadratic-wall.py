import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Define the data for the plot
x = np.logspace(1, 6, num=500)  # Values from 10^1 to 10^6
y_linear = x  # Linear scaling
y_loglinear = x * np.log(x)  # Log-linear scaling
y_quadratic = x ** 2  # Quadratic scaling

# font size
fsize=14
plt.rcParams.update({'font.size': fsize})

matplotlib.use('Agg')

# Create a stacked figure with arrow endpoints adjusted to x=6
fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Define common y-ticks based on the log scale for consistency
y_ticks = [1e2, 1e4, 1e6, 1e8, 1e10, 1e12]

# Plot 1: Log-scaled y-axis
axs[0].plot(x, y_linear, label='Linear: $O(n)$', color='green')
axs[0].plot(x, y_loglinear, label='Log-linear: $O(n \\log n)$', color='orange')
axs[0].plot(x, y_quadratic, label='Quadratic: $O(n^2)$', color='blue')
axs[0].set_xscale('log')
axs[0].set_yscale('log')
axs[0].set_yticks(y_ticks)
axs[0].set_yticklabels([f"{int(tick):,}" for tick in y_ticks])
axs[0].set_ylabel('Effort [log scale]')
axs[0].set_title('Scaling of Computational Effort (Log-Scaled Y-Axis)')
axs[0].legend()
axs[0].grid(True, which="both", linestyle='--', linewidth=0.5)

# Plot 2: Linear y-axis
axs[1].plot(x, y_linear, label='Linear: $O(n)$', color='green')
axs[1].plot(x, y_loglinear, label='Log-linear: $O(n \\log n)$', color='orange')
axs[1].plot(x, y_quadratic, label='Quadratic: $O(n^2)$', color='blue')
axs[1].set_xscale('log')
axs[1].set_yscale('linear')
axs[1].set_yticks(y_ticks)  # Use the same tick marks as the log plot
axs[1].set_yticklabels([])  # Remove tick labels to use annotations instead
axs[1].set_xlabel('Sequence Length (n) [log scale]')
axs[1].set_ylabel('Effort')
axs[1].set_title('Scaling of Computational Effort (Linear Y-Axis)')
axs[1].legend()
axs[1].grid(True, which="both", linestyle='--', linewidth=0.5)

# Adjust arrow endpoints to point at x = 6
arrow_x = 6

# Add labels and connecting lines for the linear plot with x=6 arrow endpoints
y_label_positions = np.linspace(0.1, 0.9, len(y_ticks))  # Spread labels vertically
for y_tick, y_pos in zip(y_ticks, y_label_positions):
    axs[1].annotate(f"{int(y_tick):,}", xy=(arrow_x, y_tick),  # Anchor arrows at x=6
                    xytext=(0.9, y_pos * max(y_ticks)),  # Text positions spread outside the plot area
                    arrowprops=dict(arrowstyle='-', color='black', lw=1, relpos=(1.0, 1.0)),
                    fontsize=fsize, ha='right', va='center')

# Adjust layout
plt.tight_layout()

# Show the plot
#plt.show()
plt.savefig('quadratic-wall.png')
